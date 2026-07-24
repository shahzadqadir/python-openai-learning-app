import os

from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding

from llama_index.core import (
    Settings,
    SimpleDirectoryReader,
    StorageContext,
    VectorStoreIndex,
    load_index_from_storage,
    PromptTemmplate,    
)


class DocIndexer:
    def __init__(
            self,
            llm_model: str,
            embed_model: str,
            data_folder: str,
            persist_directory: str,
            base_url: str,
            ):
        self._llm_model = llm_model
        self._emed_model = embed_model
        self._data_folder = data_folder
        self._persist_directory = persist_directory
        self._base_url = base_url
        self._query_engine = None
        self._index = None

    @property
    def llm_model(self):
        return self._llm_model

    @llm_model.setter
    def llm_model(self, value):
        self._llm_model = value

    @property
    def embed_model(self):
        return self._emed_model

    @embed_model.setter
    def embed_model(self, value):
        self._emed_model = value

    @property
    def data_folder(self):
        return self._data_folder
    
    @data_folder.setter
    def data_folder(self, value):
        self._data_folder = value

    @property
    def persist_directory(self):
        return self._persist_directory
    
    @persist_directory.setter
    def persist_directory(self, value):
        self._persist_directory = value

    @property
    def base_url(self):
        return self._base_url
    
    @base_url.setter
    def base_url(self, value):
        self._base_url = value
    
    def _set_llm_model(self):
        Settings.llm = Ollama(
            model=self.llm_model,
            base_url=self.base_url,
            request_timeout=120.0,
        )
    
    def _set_embedding_model(self):
        Settings.embed_model = OllamaEmbedding(
            model_name = self.embed_model,
            base_url = self.base_url,
        )
    
    def _load_data(self):
        if os.path.exists(self.persist_directory):
            print("Loading existing index...")
            storage_context = StorageContext.from_defaults(persist_dir=self.persist_directory)
            self._index = load_index_from_storage(storage_context)
        else:
            documents = SimpleDirectoryReader(self.data_folder).load_data()
            self._index = VectorStoreIndex.from_documents(documents)
            self._index.storage_context.persist(self.persist_directory)

    def set_query_engine(self):
        # set llm model
        self._set_llm_model()
        # set embed model
        self._set_embedding_model()
        # load documents
        self._load_data()
        # set query engine
        self._query_engine = self._index.as_query_engine()

    def ask(self, question: str):
        return self._query_engine.query(question)
