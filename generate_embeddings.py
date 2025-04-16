import os
import openai
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient

# Charger les clés du fichier .env
load_dotenv()

# Azure OpenAI
openai.api_type = "azure"
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_version = "2023-05-15"
openai.api_key = os.getenv("AZURE_OPENAI_KEY")

# Azure Search
search_client = SearchClient(
    endpoint=os.getenv("AZURE_SEARCH_ENDPOINT"),
    index_name="employee-assistant-index",
    credential=AzureKeyCredential(os.getenv("AZURE_SEARCH_KEY"))
)

# Exemple de texte
document_content = """
Bienvenue dans l’entreprise ! Pour demander un congé, connectez-vous à la plateforme RH, accédez à la section 'Congés' et remplissez le formulaire prévu.
"""

# Générer un embedding
response = openai.Embedding.create(
    input=document_content,
    engine="embedding-deploy"
)
embedding = response["data"][0]["embedding"]

# Créer le document à indexer
document = {
    "id": "doc1",
    "content": document_content,
    "contentVector": embedding
}

# Upload dans Azure AI Search
result = search_client.upload_documents(documents=[document])
print("Résultat :", result)
