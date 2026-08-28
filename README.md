# 🤖 DevOps AI Agent

A hands-on learning project where I explored **Python, DevOps automation, AWS, Docker, and Agentic AI** by building a simple DevOps AI Agent.

The agent can analyze application logs and inspect Docker containers using custom tools.

---

## 🧠 What I Learned

During this project, I practiced:

- Python fundamentals, functions, loops, conditions & data structures
- System monitoring with `psutil`
- REST APIs with **FastAPI**
- External APIs using `requests`
- AWS services using **Boto3**
- Amazon S3 file upload & bucket operations
- Running Docker commands from Python
- Log file reading and dynamic log-level analysis
- Building custom tools with **LangChain**
- Running **Llama 3.2 locally with Ollama**
- Building a tool-using **AI Agent**
- Exploring **AWS AgentCore** for agent deployment

---

## 🏗️ Architecture

```text
                    USER
                      |
                      v
              +---------------+
              |   AI AGENT    |
              |   LangChain   |
              +---------------+
                      |
             +--------+--------+
             |                 |
             v                 v
      +-------------+   +---------------+
      | Analyze Logs|   | Docker Tool   |
      +-------------+   +---------------+
             |                 |
             v                 v
         Log File         Docker CLI
             |                 |
             +--------+--------+
                      |
                      v
               +-------------+
               | Llama 3.2   |
               |   Ollama    |
               +-------------+
                      |
                      v
             DevOps AI Response
```

---

## 🔧 Tools Created

### 1. Log Analysis

The agent can read a log file and dynamically detect and count log levels.

```text
INFO
WARNING
ERROR
DEBUG
CRITICAL
FATAL
...
```

It does not depend on a predefined list of log levels.

### 2. Docker Inspection

The agent can inspect Docker containers using:

```bash
docker ps -a
```

through Python's `subprocess` module.

---

## ☁️ AWS & Python

I also practiced connecting Python applications with AWS using **Boto3**.

```text
Python
   |
 Boto3
   |
  AWS
   |
  S3
```

I learned how to:

- List S3 buckets
- Upload files to S3
- Access AWS services programmatically

---

## 🌐 FastAPI

I created a simple API with endpoints such as:

```text
GET /hello
GET /metrics
GET /aws/s3
```

Architecture:

```text
Client
  |
  v
FastAPI
  |
  +---- System Metrics → psutil
  |
  +---- AWS S3 → Boto3
```

---

## 🚀 Running the Agent

### Install dependencies

```bash
pip install langchain langchain-ollama psutil boto3 fastapi requests
```

### Start Ollama

```bash
ollama pull llama3.2
```

### Run the agent

```bash
python agent.py
```

Example prompt:

```text
Analyze C:\Python-for-DevOps\day2\app.log
```

or:

```text
Check my Docker containers
```

---

## ☁️ AgentCore

I also explored AWS AgentCore and installed its CLI:

```bash
npm install -g @aws/agentcore
```

This was my first step toward understanding how locally developed AI agents can be prepared for cloud deployment.

---

## 📚 Learning Flow

```text
Python Fundamentals
        ↓
System Monitoring
        ↓
FastAPI & APIs
        ↓
AWS + Boto3
        ↓
Docker Automation
        ↓
LangChain
        ↓
Ollama + Llama 3.2
        ↓
DevOps AI Agent
        ↓
AWS AgentCore
```

---

## 🎯 Key Takeaway

The biggest lesson from this project:

> **Don't just learn a technology — build something with it.**

I learned by writing code, breaking things, debugging them, and connecting different technologies together.

---

## 👩‍💻 Author

**Saba Ramzan**

Final-Year Computer Science Student  
DevOps and DevSecOps Engineer
Exploring **Agentic AI for DevOps**
