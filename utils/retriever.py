from dotenv import load_dotenv
import os
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import AzureOpenAIEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
load_dotenv()

def text_loader(path: str, path_type: str = "text"):
    if path_type == "text":
        loader = TextLoader(path, encoding="utf-8")
    else:
        raise ValueError(f"Unsupported source_type: {path_type}")

    document = loader.load()
    return document

def text_splitter(document: str, chunk_size: int , overlap: int):
    splitted_text= RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap
    )
    chunks=splitted_text.split_documents(document)
    return chunks

def in_memory_vector_storage(chunks: str):
    deployment_name = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT")
    embeddings=AzureOpenAIEmbeddings(
        azure_deployment=deployment_name
    )
    
    vector_store=InMemoryVectorStore(
    embeddings
    )
    vector_store.add_documents(documents=chunks)
    return vector_store.as_retriever()