# 🤖 SkillScout – AI Job Recommendation Agent

**SkillScout** is a Streamlit-based AI application that analyzes a user’s resume (PDF or Word) and provides personalized career guidance. The agent identifies your skills, recommends job roles, highlights gaps, and generates a step-by-step learning roadmap to help you advance in your career.

Powered by **LangChain** and **OpenAI GPT-4o-mini**, the app uses **Pydantic** for structured output validation to ensure reliable results.

---

## 🌟 Features

- Upload PDF or Word resumes easily
- Automatic extraction and parsing of resume text
- Analyze skills and career fit
- Recommend top job roles based on profile
- Identify missing or underdeveloped skills
- Provide a personalized learning roadmap
- Clean, interactive, and intuitive Streamlit interface

---

## 🚀 Demo

Run the app locally:

```bash
streamlit run SkillScout.py
```

Upload your resume and click **Analyze Resume** to receive:

- Recommended roles
- Skills identified
- Missing skills
- Step-by-step learning roadmap

---

## 💻 Tech Stack

- **Python 3.11+** – Stable and recommended version for ML/AI
- **Streamlit** – Frontend UI
- **LangChain** – LLM orchestration
- **OpenAI GPT-4o-mini** – AI reasoning engine
- **Pydantic** – Structured output validation
- **PyPDF / python-docx** – Resume text extraction
- **python-dotenv** – Secure management of API keys

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/swatidhoke/AI_AGENTS.git
cd AI_AGENTS
```

2. Create a virtual environment (Python 3.11 recommended):

```bash
python3.11 -m venv aiagent
source aiagent/bin/activate   # macOS / Linux
aiagent\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root:

```text
OPENAI_API_KEY=sk-your-openai-key
```

5. Run the app:

```bash
streamlit run SkillScout.py
```
<img width="1440" height="692" alt="Screenshot 2026-03-08 at 10 12 43 AM" src="https://github.com/user-attachments/assets/7ce8a97b-173a-4c92-9441-74fea5b950ff" />
<img width="796" height="701" alt="Screenshot 2026-03-08 at 10 17 53 AM" src="https://github.com/user-attachments/assets/1e9b48de-d1d9-4cef-8881-4259c9c2fdf6" />

---

## 🗂 Project Structure

```text
ai-job-agent/
│
├── SkillScout.py           # Main Streamlit app
├── requirements.txt        # Python dependencies
├── .env                    # OpenAI API key
└── README.md               # Project documentation
```

---

## 🔐 Security

- Do **not** commit your `.env` file to GitHub
- Keep your OpenAI API key private
- Use environment variables for secure key management

---
