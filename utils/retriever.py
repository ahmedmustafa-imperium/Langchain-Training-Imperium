from dotenv import load_dotenv
import os
from langchain_community.document_loaders import TextLoader, PyPDFLoader, WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import AzureOpenAIEmbeddings,AzureChatOpenAI
from langchain_core.vectorstores import InMemoryVectorStore
from langchain.retrievers import MultiQueryRetriever
load_dotenv()

def text_loader(path: str, path_type: str | None = "text"):
    if path_type:   
        if path_type == "text":
            loader = TextLoader(path, encoding="utf-8")
        elif path_type == "pdf":
            loader=PyPDFLoader(path)
        elif path_type == "web":
            loader=WebBaseLoader(path)
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

def multi_query(path:str,path_type:str):
    loadedtext=text_loader(path,path_type)
    splittedtext=text_splitter(loadedtext,chunk_size=200,overlap=20)
    vector_storage= in_memory_vector_storage(splittedtext)
    llm=AzureChatOpenAI(
        deployment_name=os.getenv("DEPLOYMENT_NAME"),
        temperature=0.6
    )
    
    return MultiQueryRetriever.from_llm(
        retriever=vector_storage,
        llm=llm,
        include_original=True
    )