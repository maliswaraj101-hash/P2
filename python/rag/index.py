import os

from qdrant_client import QdrantClient , models
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_qdrant import QdrantVectorStore



file_path = "../rag/Acumen CMS_ Company and product profile for chatbot FAQ.pdf"
loader = PyPDFLoader(file_path)

docs = loader.load()
doc_text = [doc.page_content for doc in docs]
text = "".join(doc_text)

# print(text)

text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=0)
chunks =  text_splitter.split_text(text)

# print(chunks)


embedding_model = "sentence-transformers/all-MiniLM-L6-v2"
hf = HuggingFaceEndpointEmbeddings(
    model=embedding_model,
    task="feature-extraction",
    huggingfacehub_api_token=os.environ["HUGGINGFACEHUB_API_TOKEN"],
)



qdrant_client = QdrantClient(
    url=os.environ["QDRANT_URL"],
    api_key=os.environ["QDRANT_API_KEY"],
)

# qdrant_client.create_collection(
#     collection_name="test_collectiom",
#     vectors_config=models.VectorParams(size=384, distance=models.Distance.COSINE)
# )

# print(qdrant_client.get_collections())




query = "Acumen CMS"
query_vector = hf.embed_query(query)

# print(len(query_vector))
# same 384 dimension vector by default , no worries here.

found_docs = qdrant_client.query_points(
    collection_name="test_collectiom",
    query = query_vector, # <--- Dense vector
)

print(found_docs)