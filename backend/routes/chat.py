from fastapi import APIRouter
from services.agent import run_agent
from services.database import SessionLocal
from models.interaction import Interaction

router = APIRouter()

@router.post("/chat")
def chat(data: dict):
    msg = data.get("message")
    return run_agent(msg)

@router.get("/history")
def get_history():
    db = SessionLocal()
    data = db.query(Interaction).all()

    result = [
        {
            "doctor": i.doctor,
            "products": i.products,
            "summary": i.summary,
            "date": i.date,
            "time": i.time
        }
        for i in data
    ]

    db.close()
    return result