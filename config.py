import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis .env
load_dotenv()

# --- Azure OpenAI ---
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION", "2024-12-01-preview")  # Valeur par défaut
AZURE_OPENAI_EMBEDDING_DEPLOYMENT = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT")
AZURE_OPENAI_CHAT_DEPLOYMENT = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT", "chat-gpt35")  # par défaut

# --- Azure Blob Storage ---
AZURE_BLOB_CONN_STR = os.getenv("AZURE_BLOB_CONN_STR")
AZURE_BLOB_CONTAINER = os.getenv("AZURE_BLOB_CONTAINER")

# --- Azure Search ---
AZURE_SEARCH_ENDPOINT = os.getenv("AZURE_SEARCH_ENDPOINT")
AZURE_SEARCH_KEY = os.getenv("AZURE_SEARCH_KEY")
INDEX_NAME = os.getenv("AZURE_SEARCH_INDEX_NAME", "employee-assistant-index")  # par défaut



