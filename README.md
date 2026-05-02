# 🧠 AI-CRM–HCP Interaction Module

## 📌 Overview
This project is an **AI-CRM-HCP system** designed for **Healthcare Professional (HCP) interaction logging**, built as part of a technical assignment.

It allows medical representatives to log doctor interactions using:
- 📝 Structured Form (auto-filled via AI)
- 💬 Conversational Chat Interface

The system leverages:
- LangGraph AI Agent
- Groq LLM (LLaMA 3.3 / Gemma2)
- React + Redux (Frontend)
- FastAPI (Backend)
- PostgreSQL (Database)

---

## 🚀 Key Features

### ✅ AI Chat-Based Interaction Logging
Users can type natural language like:

Met Dr. Sharma. Discussed insulin product. He was positive and asked for samples.

👉 AI automatically extracts:
- Doctor Name
- Products
- Summary
- Sentiment
- Follow-up actions

---

### ✅ Structured Form (Auto-Populated)
- Form is automatically filled using Redux state
- Read-only to simulate AI-first workflow

---

## 🤖 LangGraph AI Agent

Flow:
User Input → Router → Tool → Response → UI Update

---

## 🔧 LangGraph Tools

1. Log Interaction  
2. Edit Interaction  
3. Summarize  
4. Suggest Next Steps  
5. Get History  

---

## 🛠 Tech Stack

Frontend:
- React.js
- Redux Toolkit
- Axios

Backend:
- FastAPI
- LangGraph
- Groq LLM

Database:
- PostgreSQL

---

## ⚙️ Setup Instructions

### Backend
cd backend  
pip install -r requirements.txt  

Create .env:
GROQ_API_KEY=your_api_key

services/database.py:
DATABASE_URL = "postgresql://postgres:Your_Password@localhost:5432/ai_crm"
replace Your_Password with actual db_password

Run:
uvicorn main:app --reload  

---

### Frontend
cd frontend  
npm install  
npm start  

---

## 🧪 Example Prompts

- Met Dr. Reddy. Discussed diabetes medicine.
- Change sentiment to negative
- Suggest next steps
- Show history

---

## 👨‍💻 Author
Chetan K
