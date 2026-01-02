from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from functions.pubmed_articles import search_pubmed
from functions.diagnosis_symptoms import get_diagnosis
from functions.summarize_pubmed import summarize_text
from functions.symptom_extractor import extract_symptoms

#from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["*"]
class SymptomInput(BaseModel):
    description: str


@app.get("/")
async def root():
    return {"message": "Clinisight AI API", "endpoints": ["/docs"]}

@app.post("/diagnose")  # ← THIS WAS MISSING!

async def diagnosis(data: SymptomInput):
    symptoms = extract_symptoms(data.description)
    diagnosis_result = get_diagnosis(symptoms)
    pubmed_articles = search_pubmed("".join(symptoms)) 
    summary = summarize_text(pubmed_articles[:3000])

    return {
        "symptoms": symptoms,
        "diagnosis": diagnosis_result,
        "pubmed_articles": pubmed_articles,
        "summary": summary
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8081, reload=True)
    