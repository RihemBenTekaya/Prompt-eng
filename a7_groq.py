import os
from dotenv import load_dotenv
from groq import Groq

# Charger la clé API depuis le fichier .env
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY absente du fichier .env")

# Créer le client du fournisseur cloud
client = Groq(api_key=api_key)

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",  # Modèle à vérifier avant le TP
    messages=[{
        "role": "user",
        "content": "Explique le surapprentissage et propose deux solutions."
    }],
    temperature=0.3,
    max_completion_tokens=200
)

print(response.choices[0].message.content)

if response.usage:
    print("Tokens consommés :", response.usage.total_tokens)
