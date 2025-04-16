import os
import fitz  # PyMuPDF
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from openai import AzureOpenAI
from config import (
    AZURE_OPENAI_KEY,
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_VERSION,
    AZURE_OPENAI_EMBEDDING_DEPLOYMENT,
    AZURE_SEARCH_ENDPOINT,
    AZURE_SEARCH_KEY,
    INDEX_NAME
)


# Charger les variables d'environnement
load_dotenv()

# Clients Azure Search et Azure OpenAI
search_client = SearchClient(
    endpoint=AZURE_SEARCH_ENDPOINT,
    index_name=INDEX_NAME,
    credential=AzureKeyCredential(AZURE_SEARCH_KEY)
)


openai_client = AzureOpenAI(
    api_key=AZURE_OPENAI_KEY,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_version=AZURE_OPENAI_API_VERSION
)

# --- Extraction du texte depuis un PDF ---
def extract_text_from_pdf(file_path):
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

# --- Découpage en chunks ---
def split_into_chunks(text, max_chars=1000):
    paragraphs = text.split("\n")
    chunks, chunk = [], ""
    for p in paragraphs:
        if len(chunk) + len(p) < max_chars:
            chunk += p + "\n"
        else:
            chunks.append(chunk.strip())
            chunk = p + "\n"
    if chunk:
        chunks.append(chunk.strip())
    return chunks

# --- Génération d'embedding ---
def generate_embedding(text):
    response = openai_client.embeddings.create(
        input=text,
        model=AZURE_OPENAI_EMBEDDING_DEPLOYMENT
    )
    return response.data[0].embedding

# --- Indexation dans Azure Cognitive Search ---
def index_chunks(chunks):
    for i, chunk in enumerate(chunks):
        embedding = generate_embedding(chunk)
        document = {
            "id": f"doc-{i}",
            "content": chunk,
            "contentVector": embedding
        }
        search_client.upload_documents(documents=[document])
        print(f"✅ Chunk {i+1}/{len(chunks)} indexé")

# --- Fonction principale appelée par l'app ---
def process_and_index(file_path):
    print("📄 Extraction du texte...")
    text = extract_text_from_pdf(file_path)

    print("✂️ Découpage en morceaux...")
    chunks = split_into_chunks(text)

    print("📦 Indexation des morceaux...")
    index_chunks(chunks)

    print("🎉 Tous les chunks ont été indexés avec succès !")