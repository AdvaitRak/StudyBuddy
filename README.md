# 🤖 StudyBuddy — Your AI PDF Chat Companion

Upload your study material (PDFs) and ask questions like you're chatting with a tutor! Uses RAG + LangChain + Ollama locally.

## ✨ Features

- 🔍 Ask questions about your uploaded PDF
- 🧠 Local RAG (Retrieval-Augmented Generation) using FAISS + Gemma
- 💬 Chat memory — remembers previous questions
- 📄 Source-based answers from document
- ⚙️ Streamlit UI — simple and clean

## 🛠 Tech Stack

- LangChain 🦜🔗
- Streamlit
- Ollama (for local LLM + embeddings)
- FAISS (vector search)
- PyMuPDF / PyPDF2 (PDF parsing)

## 🚀 Getting Started

1. Clone the repo

git clone https://github.com/AdvaitRak/studybuddy.git
cd studybuddy

2. Install dependencies

uv pip install -r requirements.txt

3. Pull Ollama models

ollama pull gemma:2b
ollama pull nomic-embed-text

4. Run the app

streamlit run app1.py