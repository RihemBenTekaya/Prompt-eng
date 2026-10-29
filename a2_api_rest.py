import requests
# Adresse de l’API HTTP locale d’Ollama
API_URL = "http://localhost:11434/api/chat"
# Données de la requête (transformées en JSON par requests)
payload = {
"model": "qwen3:1.7b",
"messages": [
{"role": "user", "content": "Explique le machine learning en deux phrases."}
],
"stream": False, # Une réponse JSON complète, et non un flux
"think": False # Désactiver le raisonnement explicite si pris en charge
}
# Envoyer la requête et vérifier l'absence d'erreur HTTP
response = requests.post(API_URL, json=payload, timeout=180)
response.raise_for_status()
data = response.json() # JSON reçu -> dictionnaire Python
print("Réponse :", data["message"]["content"])
print("Modèle :", data["model"])
print("Code HTTP :", response.status_code)