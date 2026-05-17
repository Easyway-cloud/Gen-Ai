# Install before running
# pip install langchain langchain-community
# pip install pypdf sentence-transformers
# pip install faiss-cpu langchain-huggingface

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# PDF file name
file = "IPC.pdf"

# Load PDF
pdf = PyPDFLoader(file)

data = pdf.load()

# Split text
split = CharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

text = split.split_documents(data)

# Create embeddings
embed = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Create vector database
db = FAISS.from_documents(
    text,
    embed
)

# Chatbot function
def chatbot(question):

    result = db.similarity_search(
        question,
        k=1
    )

    print("\nRelevant IPC Sections:\n")

    for i, doc in enumerate(result):

        print(i + 1, ".")

        print(doc.page_content[:500])

        print("-" * 40)

# Chat loop
print("\nIPC Chatbot Ready")
print("Type 'exit' to stop\n")

while True:

    q = input("You: ")

    if q.lower() == "exit":

        print("\nChatbot: Goodbye!")

        break

    chatbot(q)
# create IPC.pdf in the same folder it should contain Section 58:
# Public servant disobeying direction of law with intent to save person from punishment...

# Section 302:
# Punishment for murder...

# Section 420:
# Cheating and dishonestly inducing delivery of property...

# Section 376:
# Punishment for rape...