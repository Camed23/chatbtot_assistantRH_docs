from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential

# Remplacez par vos informations
endpoint = "https://myrecognizerassistant.cognitiveservices.azure.com/"
key = "CPaivKOQEFKJWbXIChF8IMxX4TKhwgKLL2kcUxEfbmnHJa65n0v6JQQJ99BDACYeBjFXJ3w3AAALACOGN2ck"

# Initialisez le client
client = DocumentAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))

# Document à analyser
document_path = "C:/Users/GAMING ALIENWARE/Downloads/Document Livret d'accueil.pdf"

with open(document_path, "rb") as f:
    poller = client.begin_analyze_document("prebuilt-document", f)
    result = poller.result()

# Afficher les résultats
for page in result.pages:
    print(f"Page number: {page.page_number}")
    for line in page.lines:
        print(f"Line: {line.content}")
