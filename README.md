# AI-Enhanced Group Chat (Web App)

## Overview
This project is a **real-time group chat application** powered by **Mistral AI**.  
Multiple users can join the same chatroom, send messages, and see each other’s responses in real time.  
Any message ending with a `?` automatically triggers a response from an AI assistant using Mistral’s models.  

---

## Features
- 🔐 User authentication (JWT-based)  
- 👥 **Shared group chatroom** — all users see each other’s messages  
- 💬 Real-time chat via WebSocket  
- 🤖 AI bot replies (triggered by `?`) powered by **Mistral**  
- 📦 Clear, modular structure with `.env` configuration  
- 🛠 Easy to set up and test locally or in deployment  

---

## Prerequisites
- **OS**: Linux, macOS, or Windows  
- **MySQL 8+**  
- **Python 3.10+** and `pip`  

---

## Setup Instructions

### 1. Database Setup (MySQL)
```sql
CREATE DATABASE groupchat CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'chatuser'@'localhost' IDENTIFIED BY 'chatpass';
GRANT ALL PRIVILEGES ON groupchat.* TO 'chatuser'@'localhost';
FLUSH PRIVILEGES;
```

---

### 2. Backend (FastAPI)
```bash
cd backend
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Create `.env` and paste the following:
```ini
DATABASE_URL=mysql+asyncmy://chatuser:chatpass@localhost:3306/groupchat
JWT_SECRET=<replace_with_long_random_string>
JWT_EXPIRE_MINUTES=43200
LLM_API_BASE=https://api.mistral.ai/v1
LLM_MODEL=mistral-medium
LLM_API_KEY=<your_mistral_api_key>
APP_HOST=0.0.0.0
APP_PORT=8000
```

Run the server:
```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

Access the app at: [http://localhost:8000](http://localhost:8000)  

---

### 3. Frontend
The frontend is plain **HTML/CSS/JS** served directly by FastAPI:
- **REST API** → login, signup, and posting messages  
- **WebSocket** → broadcasting chat messages in real time  

---

## Usage

1. Start the FastAPI server (`uvicorn ...`).  
2. Open [http://localhost:8000](http://localhost:8000) in a browser.  
3. **Sign up** for an account and log in.  
4. Share the same URL with other users — each can sign up and join.  
5. All logged-in users connect to the **same group chatroom**.  
6. Messages are broadcast in real time to all participants.  
7. Any message ending with `?` will trigger an AI response from **Mistral**.  

---

## Project Structure
```
backend/
  ├── app/                # FastAPI app
  ├── requirements.txt    # Python dependencies
  └── .env.example        # Example environment configuration
frontend/
  ├── static/             # HTML, CSS, JS files
sql/
  └── schema.sql          # DB schema setup
README.md
```

---

## Best Practices Implemented
- ✅ **Detailed README** with setup & usage  
- ✅ **Environment variable configuration** (`.env`)  
- ✅ **JWT authentication** for secure sessions  
- ✅ **WebSocket broadcasting** for group messaging  
- ✅ **Clear modular structure** for easy testing  

---

## About
This project was developed as part of the **Mistral AI Internship Application**.  
