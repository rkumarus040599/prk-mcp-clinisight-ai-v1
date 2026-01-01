import requests
from bs4 import BeautifulSoup
from typing import List, Dict

import requests
import json
from typing import List, Dict

def search_pubmed(symptoms: str, max_results: int = 3) -> List[Dict]:
    """
    Pure requests PubMed API - NO Biopython needed!
    """
    
    # ESearch JSON API
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        'db': 'pubmed',
        'term': symptoms,
        'retmax': max_results,
        'retmode': 'json'
    }
    
    headers = {'User-Agent': 'MedicalBot/1.0 (your.email@example.com)'}
    
    try:
        resp = requests.get(url, params=params, headers=headers, timeout=10)
        data = resp.json()
        
        pmids = data['esearchresult']['idlist']
        if not pmids:
            return [{"title": f'No results for "{symptoms}"'}]
        
        # ESummary JSON
        summary_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
        summary_params = {
            'db': 'pubmed',
            'id': ','.join(pmids),
            'retmode': 'json'
        }
        
        resp2 = requests.get(summary_url, params=summary_params, headers=headers)
        summary_data = resp2.json()
        
        articles = []
        for pmid in pmids:
            doc = summary_data['result'][pmid]
            articles.append({
                'title': doc.get('title', 'No title'),
                'authors': doc.get('authors', []),
                'pub_date': doc.get('pubdate', 'N/A'),
                'pmid': pmid,
                'pubmed_url': f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
            })
        
        return articles
        
    except Exception as e:
        return [{"title": f'Error: {str(e)}'}]

# # Test:
# print(search_pubmed("chest pain"))
