from ollama import chat

MODELS = ["qwen3:1.7b", "gemma3:4b", "llama3.1:8b"]

PROMPT = """Un étudiant obtient 98 % d'accuracy à l'entraînement
et 68 % sur le test. Identifie le problème probable,
explique-le simplement et propose deux solutions."""

OPTIONS = {"temperature": 0, "num_predict": 250}

for model_name in MODELS:
    print(f"\n===== {model_name} =====")
    response = chat(
        model=model_name,
        messages=[{"role": "user", "content": PROMPT}],
        options=OPTIONS,
        stream=False,
        think=False
    )
    # Les durées Ollama sont données en nanosecondes
    seconds = response.total_duration / 1_000_000_000
    print(response.message.content)
    print(f"Durée totale : {seconds:.2f} s")
    print(f"Tokens générés : {response.eval_count}")
