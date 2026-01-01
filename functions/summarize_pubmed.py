import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def summarize_text(text:str) -> str:
      prompt = f"""
      Summarize the following medical extract: \n\n{text}.
      """
      
      messages = [{"role": "user", "content": prompt},
                  {"role": "system", "content": "You are a medical research summarizer."}]
      #model = "gpt-3.5-turbo"
      model = "gpt-4o-mini"

      response = client.chat.completions.create(
          model=model,
          messages=messages
          #temperature=0, # this is the degree of randomness of the model's output
          )

      return response.choices[0].message.content.strip()



