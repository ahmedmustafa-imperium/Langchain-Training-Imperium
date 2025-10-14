import os
import logging
from utils.env_loader import load_env
from langchain_openai import AzureChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory, ConversationSummaryMemory
from langchain_core.exceptions import OutputParserException
import json
import logging
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

# --- Configure file-based logging for debugging ---
logging.basicConfig(
    filename="summarizer_memory_log.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

# Load environment variables once globally
load_env()


def summarization_chain(
    memory_type: str | None = None,
    lines: int = 1,
    model_temp: float = 0.6,
    deployment_env_var: str = "DEPLOYMENT_NAME",
    verbose: bool = True
):
    """
    Create a summarization chain with optional conversational memory.

    Args:
        memory_type (str | None): "buffer" or "summary" for memory type; None for stateless chain.
        lines (int): Number of sentences in the summary (default = 1).
        model_temp (float): Model temperature for randomness (default = 0.6).
        deployment_env_var (str): Environment variable for Azure deployment name.
        verbose (bool): Whether to enable verbose output/logging in chain.

    Returns:
        LLMChain or Runnable chain (PromptTemplate | AzureChatOpenAI)
    """

    try:
        # --- Load deployment name dynamically ---
        deployment_name = os.getenv(deployment_env_var)
        if not deployment_name:
            raise EnvironmentError(
                f"❌ Missing required environment variable: {deployment_env_var}"
            )

        # --- Initialize model dynamically ---
        llm = AzureChatOpenAI(
            azure_deployment=deployment_name,
            temperature=model_temp
        )
        logging.info(
            f"Initialized AzureChatOpenAI with deployment='{deployment_name}', temperature={model_temp}"
        )

        # --- Define summarization prompt ---
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
        prompt = PromptTemplate(template=template, input_variables=["text"])
        logging.info(f"Prompt template created for {lines}-sentence summary")

        # --- Memory configuration ---
        if memory_type:
            if memory_type.lower() == "buffer":
                memory = ConversationBufferMemory(
                    memory_key="chat_history",
                    input_key="text",
                    k=3,
                    return_messages=True,
                )
                logging.info("Using ConversationBufferMemory (stores last 3 interactions)")

            elif memory_type.lower() == "summary":
                memory = ConversationSummaryMemory(
                    llm=llm,
                    memory_key="chat_history",
                    input_key="text",
                    return_messages=True,
                )
                logging.info("Using ConversationSummaryMemory (summarizes past context)")

            else:
                raise ValueError("Invalid memory type. Use 'buffer', 'summary', or None.")

            # --- Return LLMChain with memory ---
            return LLMChain(llm=llm, prompt=prompt, memory=memory, verbose=verbose)

        # --- Default: stateless summarizer (for Tasks 1–2) ---
        return prompt | llm

    except OutputParserException as lc_err:
        logging.error(f"LangChain error encountered: {lc_err}")
        raise

    except EnvironmentError as env_err:
        logging.error(f"Environment setup error: {env_err}")
        raise

    except Exception as e:
        logging.error(f"Unexpected exception in summarization_chain: {e}")
        raise


def generate_json_summary(lines: int=3):
    """
    Creates and returns the components needed for structured summarization:
    - summarization chain
    - structured output parser
    - format instructions
    """
    try:
        chain = summarization_chain(lines=lines)
        
        schemas = [
            ResponseSchema(
                name="summary",
                description=f"Summarzied version of the passage in {lines} sentences."
            ),
            ResponseSchema(
                name="length",
                description="Character count of the summary text."
            )
        ]
        
        parser=StructuredOutputParser.from_response_schemas(schemas)
        format_instructions=parser.get_format_instructions()
        logging.info("Structured output parser created successfully.")
        if hasattr(chain, "llm"):
            llm = chain.llm
        else:
        # Fallback: base_chain is a Runnable (PromptTemplate | LLM)
            llm = AzureChatOpenAI(
                azure_deployment=os.getenv("DEPLOYMENT_NAME"),
                temperature=0.6
            )
        return llm,parser,format_instructions
    except OutputParserException as parse_err:
        logging.error(f"Output parsing setup failed: {parse_err}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error preparing JSON summary chain: {e}")
        raise  
      