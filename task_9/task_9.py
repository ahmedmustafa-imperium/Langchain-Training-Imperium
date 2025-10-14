import os
from utils.summarizer import summarization_chain
from utils.env_loader import load_env
from utils.retriever import multi_query,text_loader,text_splitter,in_memory_vector_storage
from task_3.task_3 import task_3
def main():
    print("\n=== Task 9: Experimenting with Multi-Query Retrieval ===\n")

    # Load environment variables
    load_env()

    # Path to ai_intro.txt (created in Task 3)
    file_path = os.path.join("task_3", "ai_intro.txt")

    # --- Single-query retriever ---
    print("--- Using Single-Query Retriever ---")
    loadedtext = text_loader(file_path)
    splittedtext=text_splitter(loadedtext,chunk_size=200,overlap=20)
    vector_storage= in_memory_vector_storage(splittedtext)
    final_document= vector_storage.invoke("AI advancements")

    chain = summarization_chain(lines=3)
    single_summary = chain.invoke({"text": " ".join([doc.page_content for doc in final_document])}).content

    print("\nSingle-query Summary:\n", single_summary, "\n")

    # --- Multi-query retriever ---
    print("--- Using Multi-Query Retriever ---")
    multi_retriever = multi_query(file_path, path_type="text")

    # Generate alternate queries (directly from llm_chain)
    queries = multi_retriever.llm_chain.invoke("AI advancements")
    print("\nGenerated Alternate Queries:")
    for i, q in enumerate(queries, 1):
        print(f"Query {i}: {q}")

    # Fetch documents for each query separately (to inspect chunks)
    print("\nRetrieved Chunks Per Query:")
    for i, q in enumerate(queries, 1):
        docs = multi_retriever.retriever.invoke(q) 
        print(f"\n--- Chunks for Query {i}: {q} ---")
        for j, doc in enumerate(docs, 1):
            print(f"Chunk {j}: {doc.page_content[:200]}...\n")

    # Get combined retrieval (default behavior)
    docs_multi = multi_retriever.invoke("AI advancements")
    multi_summary = chain.invoke({"text": " ".join([doc.page_content for doc in docs_multi])}).content

    print("\nMulti-query Summary:\n", multi_summary, "\n")


if __name__ == "__main__":
    print("================== RUNNING TASK 9 ==================")
    main()