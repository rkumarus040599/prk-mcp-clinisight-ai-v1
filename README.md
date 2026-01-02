Clinisight AI 🚀
AI-Powered Medical Diagnosis API using FastAPI + PubMed

🎯 What it does
Send symptoms → Get AI diagnosis + PubMed research + summary in seconds!

text
"I have chest pain and fever"
↓
🔍 Extracts: ["chest", "pain", "fever"]
🤖 Diagnosis: "Possible pneumonia/flu/COVID"
📚 PubMed articles (3 latest)
📝 AI summary

🚀 Quick Start
bash
# Clone
git clone https://github.com/rkumarus040599/prk-mcp-clinisight-ai-v1.git
cd prk-mcp-clinisight-ai-v1

# Install
uv sync  # or pip install -r requirements.txt

# Run
uv run uvicorn app:app --host 127.0.0.1 --port 8081 --reload
Open: http://localhost:8081/docs 👈 Interactive tester!

🔬 API Endpoints
Method	Endpoint	Description
GET	/	Welcome + docs
POST	/diagnose	Core: Symptoms → Diagnosis + Research
Try it now!
bash
curl -X POST "http://localhost:8081/diagnose" \
  -H "Content-Type: application/json" \
  -d '{"description": "headache fever cough"}'
Response:

json
{
  "symptoms": ["headache", "fever", "cough"],
  "diagnosis": "Possible flu/viral infection",
  "pubmed_articles": ["Article 1...", "Article 2..."],
  "summary": "Research shows flu symptoms match..."
}
🏗️ Architecture
text
User Request → FastAPI → [4 AI Functions] → JSON Response
├── extract_symptoms()     # NLP: Parse text → symptoms list
├── get_diagnosis()        # ML: Symptoms → possible conditions
├── search_pubmed()        # API: Latest medical research
└── summarize_text()       # LLM: Summarize articles
📁 Project Structure
text
prk-mcp-clinisight-ai-v1/
├── app.py                 # FastAPI server
├── functions/             # Your AI modules
│   ├── diagnosis_symptoms.py
│   ├── pubmed_articles.py
│   ├── summarize_pubmed.py
│   └── symptom_extractor.py
├── requirements.txt       # Dependencies
└── .gitignore            # Clean repo
🔧 Tech Stack
Backend: FastAPI (auto-docs, type-safe)

AI/ML: Your custom functions (NLP + diagnosis)

Research: PubMed API integration

Deployment-ready: Uvicorn server

🚀 Deploy to Production