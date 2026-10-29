"""
Script de vérification de l'environnement pour TP1
Vérifie que tous les prérequis sont installés
"""

import sys

def check_module(module_name, package_name=None):
    """Vérifie si un module Python est installé"""
    if package_name is None:
        package_name = module_name
    try:
        __import__(module_name)
        print(f"✓ {package_name} est installé")
        return True
    except ImportError:
        print(f"✗ {package_name} n'est PAS installé")
        print(f"  → Installer avec: pip install {package_name}")
        return False

def check_ollama():
    """Vérifie si Ollama est accessible"""
    try:
        import requests
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        if response.status_code == 200:
            print("✓ Ollama est accessible sur localhost:11434")
            return True
        else:
            print("✗ Ollama répond mais avec un code d'erreur")
            return False
    except Exception as e:
        print("✗ Ollama n'est PAS accessible")
        print(f"  → Vérifier qu'Ollama est démarré")
        return False

def check_ollama_models():
    """Vérifie les modèles Ollama installés"""
    try:
        import requests
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        if response.status_code == 200:
            data = response.json()
            models = [model['name'] for model in data.get('models', [])]
            
            required_models = ["qwen3:1.7b", "gemma3:4b", "llama3.1:8b"]
            print("\nModèles Ollama requis :")
            all_present = True
            for model in required_models:
                if any(model in m for m in models):
                    print(f"✓ {model} est installé")
                else:
                    print(f"✗ {model} n'est PAS installé")
                    print(f"  → Installer avec: ollama pull {model}")
                    all_present = False
            return all_present
        return False
    except:
        return False

def check_env_file():
    """Vérifie l'existence du fichier .env"""
    import os
    if os.path.exists('.env'):
        print("✓ Fichier .env existe")
        # Vérifier si GROQ_API_KEY est définie
        from dotenv import load_dotenv
        load_dotenv()
        api_key = os.getenv("GROQ_API_KEY")
        if api_key and api_key != "votre_cle_api_ici":
            print("✓ GROQ_API_KEY est configurée dans .env")
            return True
        else:
            print("✗ GROQ_API_KEY n'est pas configurée dans .env")
            print("  → Ajouter: GROQ_API_KEY=votre_vraie_cle")
            return False
    else:
        print("✗ Fichier .env n'existe pas")
        print("  → Créer .env avec: GROQ_API_KEY=votre_vraie_cle")
        return False

def main():
    print("=" * 60)
    print("Vérification de l'environnement - TP1 LLM")
    print("=" * 60)
    
    print("\n📦 Vérification des bibliothèques Python :")
    modules_ok = True
    modules_ok &= check_module("requests")
    modules_ok &= check_module("ollama")
    modules_ok &= check_module("groq")
    modules_ok &= check_module("dotenv", "python-dotenv")
    
    print("\n🔌 Vérification d'Ollama :")
    ollama_ok = check_ollama()
    
    if ollama_ok:
        models_ok = check_ollama_models()
    else:
        models_ok = False
    
    print("\n🔑 Vérification de la configuration Groq :")
    env_ok = check_env_file()
    
    print("\n" + "=" * 60)
    if modules_ok and ollama_ok and models_ok:
        print("✅ Environnement prêt pour le TP !")
        if not env_ok:
            print("⚠️  Attention : configurez votre clé Groq pour A7")
    else:
        print("❌ Certains prérequis manquent")
        print("   Installez-les avant de commencer le TP")
    print("=" * 60)

if __name__ == "__main__":
    main()
