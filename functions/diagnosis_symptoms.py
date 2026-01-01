import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
def get_diagnosis(symptoms: list[str]) -> str:
      prompt = f"""
      You are a medical professional specializing in diagnosing diseases based on symptoms. 
      Given the following symptoms: {','.join(symptoms)},   Suggest some possible medical diagnosis.  
      suggest some possible cure for the same.
      """
      
      messages = [{"role": "user", "content": prompt},
                  {"role": "system", "content": "You are a medical professional specializing in diagnosing diseases based on symptoms."}]
      #model = "gpt-3.5-turbo"
      model = "gpt-4o-mini"

      response = client.chat.completions.create(
          model=model,
          messages=messages
          #temperature=0, # this is the degree of randomness of the model's output
          )

      return response.choices[0].message.content.strip()



output =  get_diagnosis(["headache", "fever","pain"])

print(output)


