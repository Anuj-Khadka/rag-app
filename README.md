# InsightOS
> A fast, lightweight RAG (Retrieval-Augmented Generation) application that lets you query custom document collections using a local Ollama LLM and ChromaDB vector database.

![InsightOS gif](documentations/vids/insightos-gif.gif)

---

## Table of Content 
- [General Info](#general-info)
- [Technologies](#technologies)
- [Glimpse](#glimpse)
- [How to Run](#how-to-run)
    - [Live Demo](#live-demo)
    - [Run Locally](#run-locally)
- [Features](#features)
- [Other Details](#other-details)

---

## General Info
**InsightOS** is a lightweight RAG (Retrieval-Augmented Generation) application built with Streamlit, ChromaDB, and Ollama. It allows users to ask questions and retrieve highly relevant information from a custom database of documents, enhancing the context before generating answers using an LLM.  
Perfect for local knowledge bases, document search engines, or personal research assistants.

---

## Technologies
- **Streamlit** (Frontend UI)
- **Ollama** (Local LLM model server)
- **ChromaDB** (Vector database for document retrieval)
- **Docker & Docker Compose** (Service orchestration)
- **Python 3.10+**

---

## Glimpse
<!-- <p>
    <img src="documentations/images/home.png" alt="InsightOS home" />
    <img src="documentations/images/query.png" alt="InsightOS query" />
    <img src="documentations/images/response.png" alt="InsightOS response" />
</p>
-->

---

## How to Run

### Live Demo
(Currently local deployment only.)

### Run Locally
- Clone the repository to your local machine:
```bash
git clone https://github.com/Anuj-Khadka/insightos.git
```
```bash
cd insightos
```
- Make sure Docker and Docker Compose are installed on your machine.
- Build and start the app:
```bash
  docker-compose up --build
```
- Open your browser and navigate to `http://localhost:8501/`.


## Features
- 🔍 Context Retrieval: Fetches the most relevant document chunks from ChromaDB based on your question.
- 🧠 Local LLM Integration: Generates AI-powered answers using locally hosted Ollama models.
- ⚡ Real-time Streaming: Watch answers generate live while you type.
- 🗂️ Flexible Document Base: Easily update or ingest new documents into ChromaDB.
- 🛡️ Fully Local: Your data and AI stay on your machine — no external APIs required.

