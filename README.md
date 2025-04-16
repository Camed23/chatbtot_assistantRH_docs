
# 🤖 Assistant RH - IA sur vos documents internes

Bienvenue dans votre assistant RH intelligent ! Cette application permet à vos collaborateurs de poser des questions RH directement à partir de documents internes (PDF, DOCX, TXT), en utilisant des technologies Microsoft Azure (Blob Storage, OpenAI, AI Search).

---

## 🚀 Fonctionnalités

- 📄 Téléversement de documents RH (PDF, DOCX, TXT)
- 🧠 Génération d'**embeddings** avec Azure OpenAI
- 🔍 Indexation des documents avec Azure AI Search
- 💬 Chatbot intelligent basé sur le modèle GPT
- ☁️ Stockage centralisé dans Azure Blob

---

## 🛠️ Technologies utilisées

- Python + Streamlit
- Azure OpenAI (embeddings + chat completions)
- Azure Cognitive Search
- Azure Blob Storage
- dotenv pour la gestion de configuration

---

## ▶️ Lancer l'application

1. Clone le projet :
   ```bash
   git clone https://github.com/Camed23/chatbtot_assistantRH_docs.git
   cd chatbtot_assistantRH_docs
   ```

2. Crée un environnement virtuel :
   ```bash
   python -m venv .venv
   source .venv/Scripts/activate  # Windows
   ```

3. Installe les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

4. Crée un fichier `.env` :
   ```env
   AZURE_OPENAI_KEY=...
   AZURE_OPENAI_ENDPOINT=...
   AZURE_OPENAI_API_VERSION=2024-12-01-preview
   AZURE_OPENAI_EMBEDDING_DEPLOYMENT=embedding-deploy
   AZURE_OPENAI_CHAT_DEPLOYMENT=chat-gpt35

   AZURE_SEARCH_ENDPOINT=...
   AZURE_SEARCH_KEY=...
   AZURE_SEARCH_INDEX_NAME=employee-assistant-index

   AZURE_BLOB_CONN_STR=...
   AZURE_BLOB_CONTAINER=...
   ```

5. Lance l’app :
   ```bash
   streamlit run app.py
   ```

---

## 📂 Structure du projet

```
📁 PythonProject
├── app.py                     # Application principale Streamlit
├── config.py                 # Chargement des variables d'environnement
├── processing_utils.py       # Extraction, découpage et indexation des documents
├── .env                      # Variables de configuration (non partagé)
├── .gitignore                # Ignore les fichiers sensibles (.venv, .env)
└── README.md                 # Ce fichier !
```

---

## 🙋‍♂️ Auteur

Développé avec 💙 par [Camed23](https://github.com/Camed23)
