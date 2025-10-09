import os
from utils.env_loader import load_env
from langchain_openai import AzureChatOpenAI
from langchain.agents import initialize_agent
from typing import Sequence

def zeroshot_agent( tools: Sequence,verbose:bool=False):
    
    load_env()
    
    deployment_name = os.getenv("DEPLOYMENT_NAME")
    
    llm= AzureChatOpenAI(
        azure_deployment=deployment_name,
        temperature=0.6
    )
    
    agent=initialize_agent(
        tools=tools,
        llm=llm,
        agent="zero-shot-react-description",
        verbose=verbose,
        handle_parsing_errors=True
    )
    
    return agent