# chatbtot_assistantRH_docs
une app Streamlit avec Azure ayant pour but de faciliter l'intégration des nouveaux employées dans une entreprise  avec un chatbot permettant uploader des fichiers et de répondre à toutes leurs questions avec des réponses cohérantes

# 🤖 Assistant RH - basé sur vos documents internes

Ce projet est une application web Streamlit permettant d’interroger des documents internes RH (PDF, DOCX, TXT) en langage naturel grâce à l'IA (RAG + Azure OpenAI + Azure Search).

---

## 🚀 Fonctionnalités

- Téléversement de fichiers RH PDF
- Extraction et découpage intelligent du contenu
- Génération d’embeddings avec Azure OpenAI
- Indexation dans Azure AI Search
- Chat intelligent avec Azure GPT-3.5 sur vos documents

---

## 🧠 Stack technique

- **Streamlit** (interface)
- **Azure Blob Storage** (stockage de fichiers)
- **Azure AI Search** (recherche vectorielle)
- **Azure OpenAI** (embeddings + chat)
- **PyMuPDF** pour l’extraction des PDF
- **Langue** : Python

---

## 📦 Installation locale

```bash
# 1. Cloner le dépôt
git clone https://github.com/Camed23/chatbtot_assistantRH_docs.git
cd chatbot_assistantRH_docs

# 2. Créer et activer un environnement virtuel
python -m venv .venv
source .venv/Scripts/activate  # sous Windows
# ou
source .venv/bin/activate  # sous Mac/Linux

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Ajouter un fichier .env avec vos clés Azure
