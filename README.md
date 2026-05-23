# Personal AI Tutor 🎓

An AI-powered tutoring platform built using Generative AI, FastAPI, Streamlit, and Gemini API.

The application provides:
- Conversational tutoring
- Step-by-step explanations
- Adaptive learning modes
- AI-generated quizzes
- Automated answer evaluation
- Context-aware tutoring with memory

---

# 🚀 Features Implemented

## ✅ Conversational AI Tutor
- Ask questions naturally
- Get detailed step-by-step explanations
- Beginner, Intermediate, and Advanced learning modes

## ✅ Teaching Modes
Different explanation styles based on student level:
- Beginner
- Intermediate
- Advanced

## ✅ Conversation Memory
The tutor remembers previous messages during the session for contextual learning.

## ✅ AI Quiz Generator
Generate quizzes dynamically for any topic:
- MCQs
- Short-answer questions
- Coding questions

## ✅ AI Answer Evaluation
Students can submit answers and receive:
- Scores
- Feedback
- Mistake analysis
- Improvement suggestions

## ✅ FastAPI Backend
REST APIs built using FastAPI.

## ✅ Streamlit Frontend
Interactive UI with chat interface and sidebar tools.

## ✅ Git & GitHub Integration
Version-controlled project with GitHub repository support.

---

# 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| Backend | FastAPI |
| LLM | Google Gemini API |
| Language | Python |
| API Communication | Requests |
| Environment Variables | python-dotenv |
| Version Control | Git + GitHub |

---

# 📁 Project Structure

```text
personal-ai-tutor/
│
├── backend/
│   ├── app.py
│   ├── tutor.py
│   ├── quiz_generator.py
│   ├── evaluator.py
│   ├── rag.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   └── app.py
│
├── data/
│
├── .gitignore
│
└── README.md
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/personal-ai-tutor.git
```

```bash
cd personal-ai-tutor
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

### Backend

```bash
cd backend
pip install -r requirements.txt
```

### Frontend

```bash
pip install streamlit requests
```

---

# 🔑 Gemini API Setup

Create a `.env` file inside `backend/`

```env
GEMINI_API_KEY=your_api_key_here
```

Get API key from:

https://aistudio.google.com

---

# ▶️ Run Backend

Inside `backend/`

```bash
uvicorn app:app --reload --port 8001
```

Backend runs at:

```text
http://127.0.0.1:8001
```

Swagger Docs:

```text
http://127.0.0.1:8001/docs
```

---

# ▶️ Run Frontend

Inside `frontend/`

```bash
streamlit run app.py
```

---

# 🧠 Current APIs

| Endpoint | Description |
|---|---|
| `/ask` | AI tutoring/chat |
| `/quiz` | Quiz generation |
| `/evaluate` | Answer evaluation |

---

# 📸 Current Workflow

## AI Tutor

```text
Student Question
      ↓
FastAPI Backend
      ↓
Gemini API
      ↓
AI Explanation
```

## Quiz + Evaluation

```text
Generate Quiz
      ↓
Student Answer
      ↓
AI Evaluation
      ↓
Feedback + Score
```

---

# 📌 Example Questions

## Tutor
- Teach me Python loops
- Explain recursion step-by-step
- What are SQL joins?

## Quiz
- Java Language
- Python Functions
- Data Structures

---

# 🔥 Future development

## 🚧 RAG Pipeline
- PDF Upload
- ChromaDB
- Embeddings
- Semantic Search
- Contextual Tutoring

## 🚧 Authentication
- Login/Signup
- User Profiles
- Progress Tracking

## 🚧 Advanced Features
- Voice tutor
- Learning analytics
- Adaptive learning
- Multi-language support

---

# 📚 Concepts Used

- Generative AI
- Prompt Engineering
- Conversational AI
- Session Memory
- REST APIs
- LLM Integration
- AI-based Evaluation
- Quiz Generation

---

# 🧑‍💻 Author

Developed as a Generative AI portfolio project to explore:
- LLM applications
- AI tutoring systems
- Educational AI
- Conversational interfaces
- AI-powered learning platforms

---

# ⭐ Future Goal

Transform this project into a complete AI-powered personalized learning platform with:
- RAG-based tutoring
- Student analytics
- Adaptive learning paths
- Document-based learning
- Multi-user authentication
- Cloud deployment