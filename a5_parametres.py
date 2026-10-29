from ollama import chat

MODEL = "gemma3:4b"

PROMPT = (
    "Propose un nom original pour une application d'aide aux révisions. "
    "Donne uniquement le nom."
)

for temp in [0.0, 0.5, 1.0]:
    print(f"\n--- temperature={temp} ---")
    response = chat(
        model=MODEL,
        messages=[{"role": "user", "content": PROMPT}],
        options={"temperature": temp, "num_predict": 100},
        stream=False
    )
    print(response.message.content)
