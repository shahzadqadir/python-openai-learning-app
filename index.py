import os
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader


load_dotenv()
openapi_key = os.environ.get('OPENAI_API_KEY')
documents = SimpleDirectoryReader('data').load_data()
index = VectorStoreIndex(documents)
query_index = index.as_query_engine()
name = query_index.query("What is candidate's name? ")
address = query_index.query("Where is the candidate's address? ")
print(name)
print(address)