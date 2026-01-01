import re

def extract_symptoms(text:str) -> list[str]:
    # Define a list of common symptoms
    common_symptoms = ["headache", "fever", "nausea", "fatigue", "pain"]
    symptoms = re.findall(r"\b(headache|fever|nausea|fatigue|pain)\b", text.lower())
    return list(set(symptoms))



#text="i am having back pain and having fever too"

#symptoms=extract_symptoms(text)

#print("Symptoms:", symptoms)

