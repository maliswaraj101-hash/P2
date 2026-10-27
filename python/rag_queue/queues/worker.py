import os

from qdrant_client import QdrantClient , models
from langchain_huggingface import HuggingFaceEndpointEmbeddings



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


def process_query(query:str):

    query_vector = hf.embed_query(query)
    found_docs = qdrant_client.query_points(
    collection_name="test_collectiom",
    query = query_vector, # <--- Dense vector
    )

    return found_docs
