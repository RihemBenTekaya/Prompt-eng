from ollama import chat

MODEL = "gemma3:4b"

SYSTEM_PROMPT = (
    "Tu es un enseignant en intelligence artificielle. "
    "Explique simplement, en français, avec un exemple concret."
)

USER_PROMPT = "Qu'est-ce que le surapprentissage ?"

response = chat(
    model=MODEL,
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": USER_PROMPT}
    ],
    stream=False
)

print(response.message.content)
