from langgraph.graph import StateGraph, END
from services.llm import llm
from typing import TypedDict
import json
from services.database import SessionLocal
from models.interaction import Interaction
from datetime import datetime

# 🧠 STATE
class AgentState(TypedDict, total=False):
    input: str
    next: str
    output: str
    data: dict

# 🔁 MEMORY
memory = {
    "last_data": {}
}

# ✅ SAFE LLM
def safe_llm(prompt):
    try:
        res = llm.invoke(prompt)
        return res.content if res else ""
    except Exception as e:
        return f"⚠️ LLM error: {str(e)}"

# 🔧 TOOL 1 — LOG
def log_interaction(state: AgentState):
    msg = state.get("input", "")

    response = safe_llm(f"""
Return ONLY valid JSON:
{{
  "doctor": "",
  "products": "",
  "summary": "",
  "sentiment": "",
  "followup": ""
}}

Input: {msg}
""")

    cleaned = response.replace("```json", "").replace("```", "").strip()

    try:
        data = json.loads(cleaned)
    except:
        data = {
            "doctor": "Unknown",
            "products": "",
            "summary": cleaned,
            "sentiment": "",
            "followup": ""
        }

    # ✅ ADD DATE + TIME AUTO
    now = datetime.now()
    data["date"] = now.strftime("%Y-%m-%d")
    data["time"] = now.strftime("%H:%M")

    # SAVE MEMORY
    memory["last_data"] = data

    # SAVE TO DB
    db = SessionLocal()
    new_entry = Interaction(**data)
    db.add(new_entry)
    db.commit()
    db.close()

    return {
        **state,
        "output": f"""
✅ Interaction Logged

Doctor: {data['doctor']}
Summary: {data['summary']}
""",
        "data": data
    }

# 🔧 TOOL 2 — EDIT
def edit_interaction(state: AgentState):
    msg = state.get("input", "")
    last_data = memory.get("last_data", {})

    response = safe_llm(f"""
Update this interaction:

Current:
{json.dumps(last_data)}

Change:
{msg}

Return JSON only:
{{
  "doctor": "",
  "products": "",
  "summary": "",
  "sentiment": "",
  "followup": ""
}}
""")

    cleaned = response.replace("```json", "").replace("```", "").strip()

    try:
        data = json.loads(cleaned)
    except:
        data = last_data

    # KEEP OLD DATE/TIME
    data["date"] = last_data.get("date")
    data["time"] = last_data.get("time")

    memory["last_data"] = data

    return {
        **state,
        "output": "✅ Interaction Updated",
        "data": data
    }

# 🔧 TOOL 3 — SUMMARY
def summarize(state: AgentState):
    msg = state.get("input", "")
    return {
        **state,
        "output": safe_llm(f"Summarize: {msg}")
    }

# 🔧 TOOL 4 — SUGGEST
def suggest_next(state: AgentState):
    msg = state.get("input", "")
    return {
        **state,
        "output": safe_llm(f"Suggest next steps: {msg}")
    }

# 🔧 TOOL 5 — HISTORY
def get_history(state: AgentState):
    db = SessionLocal()
    data = db.query(Interaction).all()
    db.close()

    output = "\n".join([f"{d.doctor} - {d.summary}" for d in data])

    return {
        **state,
        "output": f"📜 History:\n{output}"
    }

# 🤖 ROUTER
def router(state: AgentState):
    msg = state.get("input", "").lower()

    if "edit" in msg or "change" in msg or "update" in msg:
        state["next"] = "edit"
    elif "summary" in msg:
        state["next"] = "summary"
    elif "suggest" in msg:
        state["next"] = "suggest"
    elif "history" in msg:
        state["next"] = "history"
    else:
        state["next"] = "log"

    return state

# 🧠 GRAPH
builder = StateGraph(AgentState)

builder.add_node("router", router)
builder.add_node("log", log_interaction)
builder.add_node("edit", edit_interaction)
builder.add_node("summary", summarize)
builder.add_node("suggest", suggest_next)
builder.add_node("history", get_history)

builder.set_entry_point("router")

builder.add_conditional_edges(
    "router",
    lambda s: s["next"],
    {
        "log": "log",
        "edit": "edit",
        "summary": "summary",
        "suggest": "suggest",
        "history": "history",
    },
)

builder.add_edge("log", END)
builder.add_edge("edit", END)
builder.add_edge("summary", END)
builder.add_edge("suggest", END)
builder.add_edge("history", END)

graph = builder.compile()

# 🚀 RUN
def run_agent(message: str):
    result = graph.invoke({"input": message})

    return {
        "reply": result.get("output", ""),
        "data": result.get("data", {})
    }