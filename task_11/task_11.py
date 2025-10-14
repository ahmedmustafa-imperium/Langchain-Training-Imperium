from utils.tools import text_summarizer_tool,create_date_tool, create_web_search_tool
from utils.agents import zeroshot_agent


def run_task_11():
    """Run Task 11: Demonstrate tool integration using zero-shot agents."""

    summarizer_tool = text_summarizer_tool(
        name="TextSummarizer",
        lines=3,
        description="Condenses text into exactly three sentences while preserving key points."
    )

    date_tool = create_date_tool(
        name="CurrentDateTool",
        description="Returns today's date in a friendly format."
    )

    search_tool = create_web_search_tool(
        name="SimulatedWebSearch",
        description="Simulates an online search and produces a short static summary about AI."
    )

    # --- Step 2: Create Agents with Different Tool Combinations ---
    summarizer_date_agent = zeroshot_agent(
        tools=[summarizer_tool, date_tool],
        verbose=True
    )

    summarizer_search_agent = zeroshot_agent(
        tools=[summarizer_tool, search_tool],
        verbose=True
    )

    # --- Step 3: Define Test Text ---
    ai_paragraph = (
        "Artificial intelligence (AI) continues to revolutionize industries through automation, "
        "predictive analytics, and intelligent decision-making. In medicine, AI improves diagnostic "
        "accuracy and treatment planning. Financial systems rely on AI for fraud detection and "
        "market forecasting. In transport, autonomous vehicles are becoming safer and more efficient. "
        "Despite these advancements, ethical challenges such as bias, accountability, and privacy "
        "remain major discussion points for global policymakers and researchers."
    )

    # --- Test Case 1: Summarization + Date Tool ---
    print("\n=== Test 1: Summarization with Current Date ===\n")
    query_1 = "Please summarize this text and tell me what today's date is."
    response_1 = summarizer_date_agent.invoke({"input": f"{query_1}\n\n{ai_paragraph}"})
    print(response_1["output"].strip(), "\n")

    # --- Test Case 2: Summarization + Mock Search Tool ---
    print("\n=== Test 2: Summarization with Simulated Web Search ===\n")
    query_2 = "Summarize current AI developments and perform a mock web search for recent trends."
    response_2 = summarizer_search_agent.invoke({"input": query_2})
    print(response_2["output"].strip(), "\n")

    print("=== End of Task 11 ===")


if __name__ == "__main__":
    run_task_11()
