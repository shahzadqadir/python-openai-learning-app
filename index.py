from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
    Settings
)

Settings.llm = Ollama(
    model = "buddy",
    base_url = "http://host.docker.internal:11434",
    request_timeout = 120.0,
)

Settings.embed_model = OllamaEmbedding(
    model_name = "nomic-embed-text",
    base_url = "http://host.docker.internal:11434",
)

documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex(documents)

StorageContext.from_defaults(
    persist_dir="./storage2"
)

# index.storage_context.persist('./storage2')

storage_context = StorageContext.from_defaults()

query_engine = index.as_query_engine()

name = query_engine.query(
    "What is candidate's name? "
)
address = query_engine.query(
    "Where does candidate live? "
)

skills = query_engine.query(
    "what is candidate's skills summary in one line?"
)

print(name)
print(address)
print(skills)