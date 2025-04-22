# 🧠 AgenticDocs AI – Doc Summarizer & Translator

This project demonstrates a powerful multi-agent AI system built using [CrewAI](https://github.com/joaomdmoura/crewai), [Groq's LLaMA 3 model](https://groq.com/), and Python. It automatically summarizes technical documentation and translates it into a target language (Telugu in this case), showcasing agent collaboration using LLMs.

---

## 🚀 Features

- 📄 Summarizes complex robotic documentation using an LLM agent.
- 🌐 Translates summaries into regional languages via another AI agent.
- 🤝 Demonstrates effective agent collaboration using `CrewAI`.
- 🔗 Integrates external documentation sources via URLs.

---

## 🧠 How It Works

1. **Summarizer Agent**: Takes a documentation URL and generates a short, clear summary.
2. **Translator Agent**: Takes the summary and converts it into Telugu.
3. **Crew Manager**: Manages the flow of tasks and agents using the CrewAI orchestration framework.

---

## 📂 Example Use Case

Given a robotic arm product page (e.g., [`myArm M750`](https://www.elephantrobotics.com/en/myarm-m750/)), the agents will:
1. **Summarize** the technical documentation using the `Documentation Summarizer` agent.
2. **Translate** the summary into Telugu using the `Technical Translator` agent.

---

## 📁 Project Structure


AgenticDocs-AI-MAIN/
                  
                  ├── agents.py              # Defines AI agents and their configurations.
                  
                  ├── crew.py                # Initializes the Crew with agents and task.
                  
                  ├── tasks.py               # Contains individual task definitions.
                  
                  ├── requirements.txt       # List of required Python package. 
                  
                  └── README.md              # Project documentation (this file).

---

## 📦 Installation 

```bash
pip install -r requirements.txt


Also make sure to set your Groq API key in the environment:

import os
os.environ["GROQ_API_KEY"] = "<your_groq_api_key>"

