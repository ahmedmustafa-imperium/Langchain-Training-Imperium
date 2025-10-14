import os
from langchain.prompts import PromptTemplate
from langchain_openai import AzureChatOpenAI
from utils.retriever import text_loader
from utils.env_loader import load_dotenv
from utils.summarizer import summarization_chain


def qa_chain():
    """
    Build a question-answering chain that answers based only on the provided text.
    Returns a runnable chain using LCEL (| operator).
    """
    deployment_name = os.getenv("DEPLOYMENT_NAME")

    llm = AzureChatOpenAI(
        azure_deployment=deployment_name,
        temperature=0.6
    )

    template = """
    You are an AI assistant. Answer the user's question using ONLY the provided text.

    Text:
    {context}

    Question: {question}

    Answer:
    """
    prompt = PromptTemplate(
        template=template,
        input_variables=["context", "question"]
    )

    # Return LCEL chain: prompt → llm
    return prompt | llm


def main():
    print("\n=== Task 10: Building a Question-Answering Chain on Summaries ===\n")

    # Load environment
    load_dotenv()

    # Load full document (ai_intro.txt)
    docs = text_loader("task_3/ai_intro.txt")
    full_text = docs[0].page_content

    # Summarize the document
    summarizer = summarization_chain(lines=5)
    summary_text = summarizer.invoke({"text": full_text})

    # Handle LCEL vs LLMChain return formats
    if isinstance(summary_text, dict) and "text" in summary_text:
        summary_text = summary_text["text"]
    elif hasattr(summary_text, "content"):  # AIMessage
        summary_text = summary_text.content

    print("--- Document Summary ---")
    print(summary_text, "\n")

    # Build QA chain
    chain =qa_chain()

    question = "What's the key event mentioned?"

    # QA on summary
    summary_answer = chain.invoke({
        "context": summary_text,
        "question": question
    })
    if hasattr(summary_answer, "content"):
        summary_answer = summary_answer.content

    # QA on full document
    full_answer = chain.invoke({
        "context": full_text,
        "question": question
    })
    if hasattr(full_answer, "content"):
        full_answer = full_answer.content

    print("--- Q&A on Summary ---")
    print(summary_answer, "\n")

    print("--- Q&A on Full Document ---")
    print(full_answer, "\n")

    print("=== Comparison ===")
    print("- Summary-based QA → usually more concise but may miss details.")
    print("- Full-text QA → more accurate, but may include unnecessary context.")


if __name__ == "__main__":
    main()