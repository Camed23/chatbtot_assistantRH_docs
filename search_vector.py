import os
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from openai import AzureOpenAI

# Charger les variables d’environnement
load_dotenv()

# Configuration Azure AI Search
search_client = SearchClient(
    endpoint=os.getenv("AZURE_SEARCH_ENDPOINT"),
    index_name="employee-assistant-index",
    credential=AzureKeyCredential(os.getenv("AZURE_SEARCH_KEY"))
)

# Configuration Azure OpenAI
client = AzureOpenAI(
    api_version="2024-12-01-preview",  # nouvelle version
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_KEY")
)

# Question utilisateur
question = "Comment demander un congé ?"

# Requête textuelle dans l’index
results = search_client.search(
    search_text=question,
    select=["content"],
    top=3
)

# Fusionner les contenus trouvés
context = "\n\n".join([res["content"] for res in results])

# Prompt RAG
prompt = f"""Tu es un assistant RH. Réponds à la question de l'utilisateur en te basant uniquement sur le contexte suivant.

Contexte :
{context}

Question : {question}
Réponse :"""

# Appel GPT via AzureOpenAI (nouvelle méthode)
response = client.chat.completions.create(
    model="chat-gpt35",  # nom de ton déploiement GPT
    messages=[
        {"role": "system", "content": "Tu es un assistant RH utile et factuel."},
        {"role": "user", "content": prompt}
    ],
    max_tokens=800,
    temperature=0.2
)

# Affichage de la réponse
print("\nRéponse générée par l'IA :")
print(response.choices[0].message.content)
