# Clinisight AI 🚀
AI-powered symptom-to-diagnosis API built with **FastAPI** and modular Python functions.

## What this project does

- Takes a free-text symptom description from a user (for example, “chest pain and fever”).  
- Extracts structured symptoms using a symptom extraction function.  
- Generates a possible diagnosis using a diagnostic function.  
- Searches PubMed for relevant articles about the symptoms or diagnosis.  
- Summarizes the retrieved PubMed content into a concise, readable summary.

All of this is exposed via a simple HTTP API so it can be called from any frontend, script, or tool.

## Quick start

```bash
# Clone the repository
git clone https://github.com/rkumarus040599/prk-mcp-clinisight-ai-v1.git
cd prk-mcp-clinisight-ai-v1

# (Optional) create and activate a virtual environment

# Install dependencies
pip install -r requirements.txt

# Run the FastAPI app
uvicorn app:app --host 127.0.0.1 --port 8081 --reload


Then open:
Docs UI: http://127.0.0.1:8081/docs
Root endpoint: http://127.0.0.1:8081/


API endpoints

| Method | Path      | Description                          |
| ------ | --------- | ------------------------------------ |
| GET    | /         | Health check and basic info.         |
| POST   | /diagnose | Core endpoint: symptoms → diagnosis. |


Request: POST /diagnose
Body (JSON):

{
  "description": "I have chest pain and fever"
}
Response (JSON shape):

{
  "symptoms": ["chest pain", "fever"],
  "diagnosis": "Possible pneumonia or flu",
  "pubmed_articles": "...",
  "summary": "Short summary of relevant PubMed content."
}

The exact values depend on the logic in the functions module.

Project structure:

prk-mcp-clinisight-ai-v1/
├── app.py                    # HTTP API (FastAPI)
├── mcp_tool.py               # MCP Tool Server (FastMCP)
├── functions/                # Core diagnosis logic
│   ├── diagnosis_symptoms.py  # get_diagnosis(symptoms)
│   ├── pubmed_articles.py     # search_pubmed(query)
│   ├── summarize_pubmed.py    # summarize_text(text)
│   └── symptom_extractor.py   # extract_symptoms(description)  
├── requirements.txt
└── README.md



app.py wires HTTP requests into your Python functions.

The functions package holds the core logic (NLP, diagnosis, PubMed search, summarization).

How it fits in the “big picture”
Backend: FastAPI provides the HTTP server and JSON API.
Core logic: Your existing Python functions do the real work.
Integration point: Any frontend (web, CLI, MCP tool, etc.) can send a POST request to /diagnose and receive structured diagnostic output plus supporting literature.
This makes Clinisight AI a small, focused backend service that can be reused in larger AI or clinical tooling workflows.


### `mcp_tool.py` - MCP Server (FastMCP)

**Dual-interface project!** This repo provides **two ways** to use Clinisight AI:


HTTP API (app.py) → Web calls, Postman, browsers
↓
MCP Tool (mcp_tool.py) → LLM agents, MCP clients

**`mcp_tool.py` creates a FastMCP server** that exposes the exact same diagnosis pipeline as an **MCP tool**:

```python
@mcp.tool()
async def clinisight_ai(description: str) → returns diagnosis + PubMed summary

