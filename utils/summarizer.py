from utils.env_loader import load_env
import os
from langchain_openai import AzureChatOpenAI
from langchain.prompts import PromptTemplate
load_env()
def summarization_chain(lines: int = 1):
    deployment_name=os.getenv("DEPLOYMENT_NAME")
    
    llm= AzureChatOpenAI(
        azure_deployment=deployment_name,
        temperature=0.6
    )
    
    template = f"""
    Summarize the passage below into exactly {lines} sentence(s).

    Guidelines:
    - Capture only the essential information and main ideas.
    - Keep sentences clear, factual, and free of filler or commentary.
    - Do not exceed or fall short of the required number of sentences.
    - Use direct, neutral language that reflects the text's core meaning.

    Passage:
    {{text}}
    """
    
    prompt=PromptTemplate(template=template,input_variables=["text"])
    
    return prompt | llm
