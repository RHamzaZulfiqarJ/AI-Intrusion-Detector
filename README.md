<div align="center">

# 🛡️ SecureGen AI
### AI-Powered Network Intrusion Detection System

An end-to-end AI-powered cybersecurity platform that detects network intrusions using Deep Learning, explains attacks using Retrieval-Augmented Generation (RAG), and provides an interactive dashboard powered by FastAPI, Next.js, MLflow, Docker, and Kubernetes.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-2.x-red)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green)
![Next.js](https://img.shields.io/badge/Next.js-15-black)
![MLflow](https://img.shields.io/badge/MLflow-3.14-orange)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Deployed-326CE5)

</div>

---

# 📖 Overview

SecureGen AI is a production-ready AI-powered Network Intrusion Detection System developed as a Final Year Deep Learning Project.

The system combines Deep Learning with Large Language Models (LLMs) to not only classify cyber attacks but also generate human-readable explanations and mitigation strategies using Retrieval-Augmented Generation (RAG).

Unlike traditional IDS solutions, SecureGen AI provides explainable AI predictions through an interactive web dashboard while following modern MLOps practices including experiment tracking, model versioning, Docker containerization, and Kubernetes deployment.

---

# ✨ Features

- 🚀 Deep Learning Intrusion Detection
- 🤖 AI-Powered Attack Explanation
- 📚 Retrieval-Augmented Generation (RAG)
- 🔍 Similar Attack Retrieval using FAISS
- 📊 Interactive Dashboard
- ⚡ FastAPI REST API
- 🎨 Modern Next.js Frontend
- 📈 MLflow Experiment Tracking
- 🐳 Docker Containerization
- ☸ Kubernetes Deployment
- 📦 Model Registry
- 📑 Automatic Evaluation Reports

---

# 🏗️ System Architecture

```
                   +----------------+
                   |    Next.js UI  |
                   +-------+--------+
                           |
                           |
                    REST API Requests
                           |
                           ▼
                  +------------------+
                  |     FastAPI      |
                  +--------+---------+
                           |
        +------------------+-------------------+
        |                  |                   |
        ▼                  ▼                   ▼
 Deep Learning       MLflow Model       RAG Engine
 Intrusion Model      Registry          + FAISS Index
        |                  |                   |
        +------------------+-------------------+
                           |
                           ▼
                  Gemini AI Explanation
```

---

# 🧠 AI Model

Dataset:

- CICIDS2017

Model:

- Deep Neural Network (PyTorch)

Capabilities:

- Multi-class Intrusion Detection
- Attack Classification
- High Accuracy Prediction
- Real-time Inference

---

# 📚 RAG Knowledge Base

The project includes a Retrieval-Augmented Generation pipeline built using:

- LangChain
- FAISS
- Sentence Transformers
- Gemini AI

Knowledge sources include:

- MITRE ATT&CK
- NIST Publications
- OWASP Security Guidelines
- CISA Advisories

---

# 🛠️ Tech Stack

## Artificial Intelligence

- PyTorch
- NumPy
- Pandas
- Scikit-learn

## Backend

- FastAPI
- Uvicorn
- Pydantic

## Frontend

- Next.js
- TypeScript
- Tailwind CSS

## LLM

- Google Gemini
- LangChain
- Sentence Transformers

## MLOps

- MLflow 3.14
- Model Registry
- Experiment Tracking

## Deployment

- Docker
- Kubernetes

---

# 📂 Project Structure

```
Final Project
│
├── backend/
├── frontend/
├── src/
│   ├── preprocessing/
│   ├── training/
│   ├── inference/
│   ├── rag/
│   ├── llm/
│   ├── evaluation/
│   └── mlops/
│
├── artifacts/
├── kubernetes/
├── notebooks/
├── data/
├── training/
└── docker-compose.yml
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/securegen-ai.git

cd securegen-ai
```

---

## Create Environment

```bash
conda create -n securegen python=3.12

conda activate securegen
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Training

```bash
python -m src.training.train
```

---

# 🌐 Run Backend

```bash
uvicorn backend.app.main:app --reload
```

Swagger:

```
http://localhost:8000/docs
```

---

# 💻 Run Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend:

```
http://localhost:3000
```

---

# 📊 MLflow

Start MLflow

```bash
mlflow ui
```

Open

```
http://localhost:5000
```

---

# 🐳 Docker

Build

```bash
docker build -t intrusion-detector:v1 .
```

Run

```bash
docker run -p 8000:8000 intrusion-detector:v1
```

---

# ☸ Kubernetes

Deploy

```bash
kubectl apply -k kubernetes
```

Verify

```bash
kubectl get all -n intrusion-detector
```

---

# 📸 Screenshots

Add screenshots here.

```
screenshots/

├── dashboard.png
├── prediction.png
├── mlflow.png
├── swagger.png
├── docker.png
└── kubernetes.png
```

---

# 📈 MLOps

Implemented Features

- Experiment Tracking
- Model Registry
- Dataset Metadata
- Artifact Logging
- System Metadata
- Metrics Logging
- Parameters Logging
- Model Versioning

---

# 🎯 Future Improvements

- CI/CD Pipeline
- Prometheus Monitoring
- Grafana Dashboard
- Model Drift Detection
- Auto Retraining
- Cloud Deployment
- Multi-Node Kubernetes

---

# 👨‍💻 Team Members

| Name | Student ID |
|------|------------|
| Hamza Zulfiqar | F2023376057 |

---

# 📜 License

This project is developed for academic purposes as a Semester Final Deep Learning Project.

---

<div align="center">

### ⭐ If you like this project, consider giving it a star!

Made with ❤️ using PyTorch, FastAPI, Next.js, MLflow & Kubernetes.

</div>
