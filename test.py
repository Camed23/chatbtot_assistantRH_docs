from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv
import os

load_dotenv()

search_client = SearchClient(
    endpoint=os.getenv("AZURE_SEARCH_ENDPOINT"),
    index_name="employee-assistant-index",
    credential=AzureKeyCredential(os.getenv("AZURE_SEARCH_KEY"))
)

results = search_client.search(search_text="*", top=10)

print("Documents actuellement présents dans l'index :\n")
for res in results:
    print(res["id"], ":", res["content"])