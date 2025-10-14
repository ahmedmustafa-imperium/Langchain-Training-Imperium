import logging
from langchain_core.exceptions import OutputParserException
from utils.tools import text_summarizer_tool, retrieval_tool, word_count_tool
from utils.agents import zeroshot_agent


# --- Configure file-based logging for debugging ---
logging.basicConfig(
    filename="agent_execution.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)


def configure_tools(
    source_path: str = "task_3/ai_intro.txt",
    summary_sentences: int = 3,
    enable_word_counter: bool = True
):
    """
    Dynamically configure and return toolset based on parameters.
    """

    try:
        retriever = retrieval_tool(
            path=source_path,
            name="Retriever",
            description="Retrieves relevant text chunks from the provided file based on query.",
        )

        summarizer = text_summarizer_tool(
            name="Summarizer",
            lines=summary_sentences,
            description=f"Generates a concise summary in exactly {summary_sentences} sentences.",
        )

        tools = [retriever, summarizer]

        if enable_word_counter:
            word_counter = word_count_tool(
                name="WordCounter",
                description="Counts the number of words in a given text summary.",
            )
            tools.append(word_counter)

        logging.info(f"Configured {len(tools)} tools successfully.")
        return tools

    except Exception as e:
        logging.error(f"Error configuring tools: {e}")
        raise


def create_agent(tools, verbose: bool = False):
    """
    Initialize and return a zero-shot agent with the given tools.
    """

    try:
        agent = zeroshot_agent(tools=tools, verbose=verbose)
        logging.info("Agent initialized successfully.")
        return agent

    except Exception as e:
        logging.error(f"Agent initialization failed: {e}")
        raise


def execute_agent_tasks(agent, queries: list[str]):
    """
    Dynamically executes a list of queries using the provided agent.
    """

    for idx, query in enumerate(queries, start=1):
        try:
            logging.info(f"Executing query {idx}: {query}")
            result = agent.invoke({"input": query})

            print(f"\n=== Execution {idx}: Query Output ===\n")
            print(result["output"].strip(), "\n")

        except OutputParserException as parse_err:
            logging.error(f"Parsing error during agent execution: {parse_err}")
            print(f"⚠️ Parsing error while processing query {idx}: {parse_err}")

        except Exception as e:
            logging.error(f"Unhandled exception on query {idx}: {e}")
            print(f"❌ Unexpected error on query {idx}: {e}")


def main():
    # --- Default dynamic configuration ---
    print("================== RUNNING TASK 5 ==================")
    tools = configure_tools(
        source_path="task_3/ai_intro.txt",
        summary_sentences=3,
        enable_word_counter=True
    )

    # Create the agent dynamically based on tools list
    agent = create_agent(tools, verbose=True)

    # Define dynamic queries (can be modified easily)
    queries = [
        "Locate and summarize details about key AI breakthroughs from the file.",
        "Find content about AI milestones, summarize it, and include a word count."
    ]

    execute_agent_tasks(agent, queries)


if __name__ == "__main__":
    main()
