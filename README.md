TP1 : Prise en main des LLM - API REST, SDK et Python

Cours: Prompt Engineering & Agentic AI  
Enseignant : Dr. Ing. Rihab LAAJILI  

---

 Objectifs du TP

- Interroger un LLM local (Ollama) depuis le terminal et Python
- Exploiter une API REST et un SDK pour envoyer des requêtes
- Configurer les messages system/user et les paramètres d'inférence
- Comparer trois modèles et interpréter leurs résultats
- Interroger un LLM cloud (Groq) en protégeant une clé API

---

 Structure du projet

```
prompt/
├── a2_api_rest.py          # A2 - Appel direct API REST Ollama
├── a3_sdk_ollama.py        # A3 - Utilisation du SDK Ollama
├── a4_messages.py          # A4 - Messages system et user
├── a5_parametres.py        # A5 - Paramètres d'inférence (temperature, num_predict)
├── a6_comparaison.py       # A6 - Comparaison de 3 modèles
├── a7_groq.py              # A7 - Appel API cloud Groq
├── check_environment.py    # Script de vérification de l'environnement
├── .env.example            # Exemple de fichier de configuration
├── .env                    # Votre fichier de configuration (À CRÉER, NE PAS PARTAGER)
├── GUIDE_TP1.md           # Guide détaillé pour chaque exercice
└── README.md              # Ce fichier
```

---

 Démarrage rapide

1. Vérifier l'environnement

```powershell
python check_environment.py
```

Ce script vérifie :
- ✓ Installation des bibliothèques Python (requests, ollama, groq, python-dotenv)
- ✓ Accessibilité d'Ollama (localhost:11434)
- ✓ Présence des modèles requis (qwen3:1.7b, gemma3:4b, llama3.1:8b)
- ✓ Configuration de la clé API Groq

2. Configurer la clé API Groq (pour A7)

```powershell
# Copier l'exemple
copy .env.example .env

# Éditer .env et ajouter votre vraie clé
# GROQ_API_KEY=gsk_...
```


3. Exécuter les exercices dans l'ordre

```powershell
# A1 - Terminal (voir GUIDE_TP1.md)
ollama run qwen3:1.7b

# A2 - API REST
python a2_api_rest.py

# A3 - SDK Ollama
python a3_sdk_ollama.py

# A4 - Messages
python a4_messages.py

# A5 - Paramètres
python a5_parametres.py

# A6 - Comparaison (⏱️ peut prendre plusieurs minutes)
python a6_comparaison.py

# A7 - Groq Cloud
python a7_groq.py
```

---

 Prérequis

Logiciels requis

- Python 3.8+
- VS Code
- Ollama (installé et démarré)

Bibliothèques Python

```powershell
pip install requests ollama groq python-dotenv
```

 Modèles Ollama

```powershell
ollama pull qwen3:1.7b
ollama pull gemma3:4b
ollama pull llama3.1:8b
```

Compte Groq (pour A7)

1. Créer un compte sur [console.groq.com](https://console.groq.com)
2. Générer une clé API
3. L'ajouter dans le fichier `.env`

---




Concepts clés abordés

 API REST vs SDK
- **API REST** : Communication HTTP directe (requêtes POST/GET)
- **SDK** : Bibliothèque qui encapsule les appels HTTP

 Messages LLM
- **system** : Définit le comportement général du modèle
- **user** : Contient la requête spécifique

Paramètres d'inférence
- **temperature** : Contrôle la créativité (0 = déterministe, 1+ = créatif)
- **num_predict** : Limite maximale de tokens générés

 Local vs Cloud
- **Local (Ollama)** : Confidentialité, pas d'Internet, ressources locales
- **Cloud (Groq)** : Performance, scalabilité, clé API requise

---


