import os
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding

Settings.llm = Ollama(
    model="buddy",
    base_url="http://host.docker.internal:11434",
    request_timeout=120.0
)

Settings.embed_model = OllamaEmbedding(
    model_name="nomic-embed-text",
    base_url="http://host.docker.internal:11434",
)

documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex(documents)


query_engine = index.as_query_engine()

name = query_engine.query(
    "What is candidate's name? "
)

address = query_engine.query(
    "What is candidate's address?"
)

print(name)
print(address)