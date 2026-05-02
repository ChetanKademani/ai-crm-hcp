# 🧠 AI-First CRM – HCP Interaction Module

## 📌 Overview
This project is an **AI-first CRM system** designed for **Healthcare Professional (HCP) interaction logging**.

The goal is to replace traditional manual CRM entry with an **AI-powered workflow**, where medical representatives can log interactions using natural language.

The system supports:
- 💬 Conversational AI logging (primary)
- 📝 Structured form (auto-filled by AI)

---

## 🚀 Key Features

### ✅ AI Chat-Based Interaction Logging
Users can type natural language like:

Met Dr. Sharma. Discussed insulin product. He was positive and asked for samples.

👉 The AI automatically extracts:
- Doctor Name
- Products discussed
- Interaction summary
- Sentiment
- Follow-up actions

---

### ✅ Structured Form (Auto-Populated)
- Form is automatically filled using Redux state
- Read-only to simulate AI-first workflow
- Eliminates manual data entry

---

## 🤖 LangGraph AI Agent (Core Requirement)

This system uses a **LangGraph agent** to manage interaction workflows.

### 🔁 How it works:
1. User sends input via chat
2. LangGraph **router** analyzes intent
3. Based on intent, the correct tool is executed
4. Output is returned and UI updates automatically

---

## 🔧 LangGraph Tools

### 1. Log Interaction (MANDATORY)
- Converts natural language → structured JSON using LLM
- Extracts key fields (doctor, summary, sentiment, etc.)
- Stores data in PostgreSQL
- Automatically adds date & time

---

### 2. Edit Interaction (MANDATORY)
- Updates the last logged interaction
- Uses memory to retrieve previous data
- Keeps original timestamp intact

Example:
Change sentiment to negative

---

### 3. Summarize Tool
- Generates concise summaries of interaction notes

---

### 4. Suggest Next Steps
- Recommends follow-up actions for medical reps

---

### 5. Get History
- Fetches all previous interactions from database

---

## 🧠 Architecture

User → Chat UI → FastAPI → LangGraph Router → Tool Execution → Database → Response → UI

---

## 🛠 Tech Stack

### Frontend
- React.js
- Redux Toolkit
- Axios

### Backend
- FastAPI
- LangGraph
- Groq LLM (LLaMA 3.3 / Gemma2)

### Database
- PostgreSQL

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository
git clone <your-repo-link>  
cd ai-crm-hcp  

---

### 2️⃣ Backend Setup
cd backend  
pip install -r requirements.txt  

Create `.env` file:
GROQ_API_KEY=your_api_key  

Run backend:
uvicorn main:app --reload  

---

### 3️⃣ Database Setup
- Ensure PostgreSQL is running
- services/database.py: DATABASE_URL = "postgresql://postgres:Your_Password@localhost:5432/ai_crm"
- Update DATABASE_URL in backend config

Tables are created automatically on startup.

---

### 4️⃣ Frontend Setup
cd frontend  
npm install  
npm start  

---

## 🧪 Example Prompts

- Met Dr. Reddy. Discussed diabetes medicine. He seemed positive.
- Change sentiment to negative
- Suggest next steps
- Show history

---

## 📌 What I Understood

This assignment emphasizes:
- AI-first user experience over manual entry
- Automating CRM workflows using LLMs
- Using LangGraph as an intelligent decision engine
- Real-world pharmaceutical sales use case

---

## 📈 Future Improvements
- Voice-to-text interaction logging
- Multi-HCP interaction support
- Analytics dashboard
- Offline support for field representatives

---

## 👨‍💻 Author
Chetan K
