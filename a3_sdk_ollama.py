from ollama import chat

MODEL = "qwen3:1.7b"

# Le SDK prépare la requête et convertit la réponse
response = chat(
    model=MODEL,
    messages=[{"role": "user", "content": "Explique le deep learning en deux phrases."}],
    think=False,
    stream=False
)

print("Réponse :", response.message.content)
print("Modèle :", response.model)
