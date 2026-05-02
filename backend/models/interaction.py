from sqlalchemy import Column, Integer, String, Text
from services.database import Base

class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    doctor = Column(String)
    products = Column(String)
    summary = Column(Text)
    sentiment = Column(String)
    followup = Column(Text)
    date = Column(String)
    time = Column(String)