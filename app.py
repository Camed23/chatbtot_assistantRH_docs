import streamlit as st
import os
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
from processing_utils import process_and_index
from config import (
    AZURE_BLOB_CONN_STR,
    AZURE_BLOB_CONTAINER,
    AZURE_OPENAI_KEY,
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_VERSION,
    AZURE_OPENAI_CHAT_DEPLOYMENT,
    AZURE_SEARCH_ENDPOINT,
    AZURE_SEARCH_KEY,
    INDEX_NAME
)

from openai import AzureOpenAI
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient

# Initialiser le BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(AZURE_BLOB_CONN_STR)
container_client = blob_service_client.get_container_client(AZURE_BLOB_CONTAINER)

# --- UI ---
st.set_page_config(page_title="Assistant RH", layout="wide")
st.markdown("""
    <h1 style='color: white;'>Assistant RH - basé sur vos documents internes 📄🧠</h1>
    <p>Posez votre question sur l'entreprise, les congés, les primes...</p>
""", unsafe_allow_html=True)

# Upload du document
uploaded_file = st.file_uploader("Téléversez un document RH (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"])

if uploaded_file:
    file_name = uploaded_file.name
    file_bytes = uploaded_file.read()

    # Upload vers Azure Blob Storage
    container_client.upload_blob(name=file_name, data=file_bytes, overwrite=True)
    st.success(f"🌟 Fichier '{file_name}' envoyé dans Azure Blob Storage avec succès.")

    # Sauvegarder temporairement en local pour traitement
    local_path = f"./temp_files/{file_name}"
    os.makedirs(".venv/temp_files", exist_ok=True)
    with open(local_path, "wb") as f:
        f.write(file_bytes)

    # Traitement et indexation
    process_and_index(local_path)
    st.success("🚀 Fichier traité et indexé avec succès dans Azure AI Search.")

# Barre de question
st.markdown("<hr>", unsafe_allow_html=True)
question = st.text_input("Votre question :")

if st.button("🧐 Interroger les documents") and question:
    client = AzureOpenAI(
        api_key=AZURE_OPENAI_KEY,
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        api_version=AZURE_OPENAI_API_VERSION
    )

    search_client = SearchClient(
        endpoint=AZURE_SEARCH_ENDPOINT,
        index_name=INDEX_NAME,
        credential=AzureKeyCredential(AZURE_SEARCH_KEY)
    )

    results = search_client.search(search_text=question, select=["content"], top=3)
    context = "\n\n".join([res["content"] for res in results])

    prompt = f"""Tu es un assistant RH. Réponds à la question de l'utilisateur en te basant uniquement sur le contexte suivant.

Contexte :
{context}

Question : {question}
Réponse :"""

    response = client.chat.completions.create(
        model="chat-gpt35",
        messages=[
            {"role": "system", "content": "Tu es un assistant RH utile et factuel."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=800,
        temperature=0.2
    )

    st.markdown("""<div style='margin-top: 20px; background-color: #154734; padding: 1rem; border-radius: 8px;'>
    <strong style='color: white;'>Réponse de l'assistant RH :</strong>
    </div>""", unsafe_allow_html=True)
    st.write(response.choices[0].message.content)
