from langchain.agents import Tool
from utils.summarizer import summarization_chain
from utils.retriever import text_loader, text_splitter,in_memory_vector_storage
from datetime import date
from langchain.tools import Tool
from langchain_community.tools.ddg_search import DuckDuckGoSearchRun

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
    text=text_splitter(text,200,20)
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

def create_date_tool(
    name: str = "CurrentDateTool",
    description: str | None = None,
) -> Tool:
    """
    Creates a simple tool that returns the current system date in a readable format.
    """
    description = description or "Provides the current date in 'Month Day, Year' format."

    def _fetch_date(_: str = "") -> str:
        today_date = date.today().strftime("%B %d, %Y")
        return f"The current date is {today_date}."

    return Tool(
        name=name,
        func=_fetch_date,
        description=description
    )


def create_web_search_tool(name: str = "WebSearch", description: str | None = None) -> Tool:
    """
    A real web search tool using DuckDuckGoSearchRun from LangChain.
    """
    if description is None:
        description = "Searches the web using DuckDuckGo and returns summarized results."

    search = DuckDuckGoSearchRun()

    def _search(query: str) -> str:
        try:
            result = search.run(query)
            return f"Search Results: {result}"
        except Exception as e:
            return f"Search failed: {e}"

    return Tool(name=name, func=_search, description=description)
