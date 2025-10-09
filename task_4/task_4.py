from utils.env_loader import load_env
from utils.tools import text_summarizer_tool
from utils.agents import zeroshot_agent

def main():
    summary=text_summarizer_tool(
        name="TextSummarizer",
        lines=3,
    )
    
    agent=zeroshot_agent(
        tools=[summary],verbose=False
    )
    
    healthcare_text = """
    Artificial Intelligence is transforming healthcare by enhancing diagnosis accuracy, predicting diseases, and improving patient care. 
    Machine learning algorithms analyze medical images faster and with higher precision, enabling early detection of conditions like cancer or heart disease. 
    AI systems assist doctors in personalizing treatment plans and optimizing hospital workflows. 
    Natural language processing automates record keeping and extracts key insights from clinical notes. 
    Predictive analytics helps forecast patient risks and resource needs. 
    Despite these benefits, challenges remain regarding data privacy, bias, and accountability. 
    Overall, AI promises a more efficient, accessible, and proactive healthcare ecosystem for patients worldwide.
    """
    
    prompt = (
    "Apply the TextSummarizer tool to the following passage.\n"
    "Summarize the impact of AI on healthcare\n\n"
    f"{healthcare_text}"
    )

    response = agent.invoke({"input": prompt})
    print("3-lines Summary on AI in Healthcare\n")
    print(response["output"].strip(), "\n")
    
    prompt = (
    "Apply the TextSummarizer tool to the following passage.\n"
    "Summarize something interesting\n\n"
    f"{healthcare_text}"
    )

    response = agent.invoke({"input": prompt})
    print("3-Lines Summary on something interesting\n")
    print(response["output"].strip(), "\n")



if __name__=="__main__":
    main()