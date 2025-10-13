from utils.retriever import text_loader, text_splitter,in_memory_vector_storage
from utils.summarizer import summarization_chain
from task_2.task_2 import summary
def main(path:str,path_type: str):
    loadedtext=text_loader(path=path,path_type=path_type)
    #print(f"Sample page content:\n{loadedtext[0].page_content[:300]}")
    splittedtext=text_splitter(loadedtext,chunk_size=150,overlap=30)
    vector_storage= in_memory_vector_storage(splittedtext)
    final_document= vector_storage.invoke("AI Milestones")
    print("Final document\n",final_document)
    
    summary(final_document)

if __name__=="__main__":
    print("PDF Query\n")
    main("task_7\AI_Ethics_Report.pdf","pdf")
    print("WEB Query\n")
    main("https://en.wikipedia.org/wiki/Artificial_intelligence","web")