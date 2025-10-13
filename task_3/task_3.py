from utils.retriever import text_loader, text_splitter,in_memory_vector_storage
from task_2.task_2 import summary
def main():
    loadedtext=text_loader("task_3/ai_intro.txt")
    splittedtext=text_splitter(loadedtext,chunk_size=200,overlap=20)
    vector_storage= in_memory_vector_storage(splittedtext)
    final_document= vector_storage.invoke("AI Milestones")
    print("Final document\n",final_document)
    
    summary(final_document)

if __name__=="__main__":
    main() 