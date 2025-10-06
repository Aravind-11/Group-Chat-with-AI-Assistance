# AI-Enhanced Group Chat (Web App)

## Overview
This project is a **real-time group chat application** with AI Assistance.

Multiple users can join the same chatroom, send messages, and see each other’s responses in real time.  
Any message ending with a `?` automatically triggers a response from an AI assistant using Mistral’s models.  
Each AI response can be **liked or disliked** by users, and the collected feedback is used in a **preference fine-tuning loop** with **GRPO** to continuously improve model behavior.  

---
![Group Chat Interface](backend/chat.png)

## Features
- 🔐 User authentication (JWT-based)  
- 👥 **Shared group chatroom** — all users see each other’s messages  
- 💬 Real-time chat via WebSocket  
- 🤖 AI bot replies (triggered by `?`) powered by **Mistral**  
- 👍👎 **Feedback system** — like/dislike buttons on each AI response  
- 🔄 **Feedback-to-fine-tuning loop** using **GRPO** for preference adaptation  
- 📦 Clear, modular structure with `.env` configuration  
- 🛠 Easy to set up and test locally or in deployment  

---

## Prerequisites
- **OS**: Linux, macOS, or Windows  
- **MySQL 8+**  
- **Python 3.10+** and `pip`  

---

## (Option 1) Setup Instructions (To run locally)

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

## (Option 2) 🚀 Run with Docker (Recommended)

This setup lets you run the **FastAPI + MySQL + Frontend** stack using Docker Compose — no manual environment setup required.

---

### 1️⃣ Build and Run Containers

From the project root:

```bash
docker compose up --build
```
---

### 3. Frontend
The frontend is **HTML/CSS/JS** served by FastAPI:
- **REST API** → login, signup, and posting messages  
- **WebSocket** → broadcasting chat messages in real time  
- **Feedback UI** → like/dislike buttons on AI messages  

---

## Usage

1. Start the FastAPI server (`uvicorn ...`).  
2. Open [http://localhost:8000](http://localhost:8000) in a browser.  
3. **Sign up** for an account and log in.  
4. Share the same URL with other users — each can sign up and join.  
5. All logged-in users connect to the **same group chatroom**.  
6. Messages are broadcast in real time to all participants.  
7. Any message ending with `?` will trigger an AI response from **Mistral**.  
8. Users can **like or dislike** AI responses.  
9. Feedback is stored in the DB and used in a **GRPO fine-tuning pipeline** to improve model responses over time.  

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

