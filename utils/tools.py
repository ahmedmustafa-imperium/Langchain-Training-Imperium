from langchain.agents import Tool
from utils.summarizer import summarization_chain

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