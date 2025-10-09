from langchain.agents import Tool
from utils.summarizer import summarization_chain
from utils.retriever import text_loader, text_splitter,in_memory_vector_storage

def text_summarizer_tool(
    name: str = "TextSummarizer",
    lines: int =3,
    description: str | None = None,
) -> Tool:
    """
    Factory function to create a LangChain Tool for summarization.

    Args:
        name (str): Tool name (displayed to the agent)
        lines (int): Number of sentences in the summary
        description (str): Optional custom tool description
    Returns:
        Tool: Configured LangChain Tool ready to be used in agents
    """
    chain = summarization_chain(lines=lines)
    
    if description is None:
        description = (
            f"Summarize the passage into exactly {lines} sentence(s)"
        "Input: plain text. Output: summary as a string."
        )
        
        
    
    def summarize_text(text: str) -> str:
        """Internal function that runs the summarizer chain."""
        result = chain.invoke({"text": text})
        return result.content
    
    
    return Tool(
        name=name,
        func=summarize_text,
        description=description
        )
    
def retrieval_tool(
    path: str,
    name:str="TextRetriver",
    description: str |None=None
)-> Tool:
    """Wrap Task 3 retriever as a LangChain Tool."""
    text=text_loader(path)
    text=text_splitter(text)
    retriever=in_memory_vector_storage(text)

    if description is None:
        description = (
            "Retrieves relevant chunks from a document based on a query. "
            "Input: a search query string. Output: retrieved text passages."
        )

    def _retrieve(query: str) -> str:
        docs = retriever.invoke(query)
        return "\n\n".join([doc.page_content for doc in docs])

    return Tool(name=name, func=_retrieve, description=description)

def word_count_tool(
    name: str = "WordCounter",
    description: str | None = None,
) -> Tool:
    """Simple tool to count words in a given text."""
    if description is None:
        description = "Counts the number of words in the given text string."

    def _count(text: str) -> str:
        count = len(text.split())
        return f"Word count: {count}"

    return Tool(name=name, func=_count, description=description)