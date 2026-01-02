from mcp.server.fastmcp import FastMCP
from functions.pubmed_articles import search_pubmed
from functions.diagnosis_symptoms import get_diagnosis
from functions.summarize_pubmed import summarize_text
from functions.symptom_extractor import extract_symptoms

mcp = FastMCP('Clinisight AI')

@mcp.tool()
async def clinisight_ai(description: str):
    symptoms = extract_symptoms(description)
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
    mcp.run(transport='stdio')