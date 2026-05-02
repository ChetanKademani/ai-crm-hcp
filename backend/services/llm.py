import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.3-70b-versatile"
)

def test_llm():
    try:
        res = llm.invoke("Say hello")
        return res.content
    except Exception as e:
        return f"LLM Error: {str(e)}"