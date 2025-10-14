# 🧠 LangChain Training Task – Environment Variable Loader  
### 👤 Owner: Ahmed Mustafa  

This project is part of a **training assignment** aimed at understanding how environment configuration works in Python before integrating it with **LangChain** and related tools.  
The goal is to learn how to securely manage API keys and endpoints that will later be used in LangChain applications.

---

# Task 1 – Environment Variable Loader

## 📘 Overview
This project demonstrates how to load and validate environment variables in Python using the `python-dotenv` package.  
It consists of two main scripts:

1. **`env_loader.py`** – Responsible for loading environment variables from a `.env` file.  
2. **`task1.py`** – Main script that validates whether all required environment variables are set correctly.

---

## 🧩 What I Did
- Implemented a function to load environment variables using `dotenv`.  
- Created a script (`task1.py`) that:
  - Loads environment variables.  
  - Checks if all required keys are set.  
  - Displays partially masked values for security.  
  - Raises an error if any variable is missing.

---

## 💡 What I Understood
- Environment variables store sensitive information like API keys securely outside the codebase.  
- The **`python-dotenv`** package simplifies loading these variables from a `.env` file.  
- Using **`os.getenv()`**, you can retrieve the values of these variables in Python.  
- Masking sensitive data prevents accidental exposure in logs or terminal output.  
- Proper error handling ensures missing variables are identified early.

---

# Task 2 – AI Text Summarizer   

This project is part of my **LangChain training tasks**, focused on understanding how to use **LangChain** with **Azure OpenAI** to build a simple **text summarization chain**.  
The goal is to practice prompt templates, chains, and Azure model configuration in LangChain.

---

## 📘 Overview
This project uses **LangChain** and **Azure OpenAI** to summarize text into different lengths using an LLM (Large Language Model).  

It consists of:
1. **`summarizer.py`** – Defines the `summarization_chain()` function using LangChain’s prompt and LLM tools.  
2. **`task_2.py`** – Loads text input, invokes the summarizer for both 3-line and 1-line summaries, and displays the results.

---

## 🧩 What I Did
- Loaded environment variables securely using the `.env` file via `load_env()`.  
- Created an **AzureChatOpenAI** instance to connect to the Azure OpenAI model defined in environment variables.  
- Built a **PromptTemplate** to structure summarization instructions.  
- Used the LangChain **pipe operator (`|`)** to connect the prompt and the model into a single chain.  
- Invoked the summarizer to generate both short (1 line) and slightly longer (3 line) summaries of the same text.  

---

## 💡 What I Understood
- How to integrate **Azure OpenAI** with **LangChain** using environment variables for secure access.  
- The role of **PromptTemplate** in controlling how LLMs respond.  
- How **LangChain chains** link multiple components together (`prompt | llm`).  
- How to call a LangChain chain with `.invoke()` to pass input and get model output.  
- How to structure and format output summaries cleanly.

---

# Task 3 – Text Retrieval and Summarization   

This project is part of my **LangChain Training Series**, focused on learning how to use **retrievers**, **embeddings**, and **vector stores** in LangChain.  
In this task, I built a small pipeline that loads a document, splits it into chunks, stores embeddings in memory, retrieves relevant text based on a query, and then summarizes the result using the summarization chain from **Task 2**.

---

## 📘 Overview
This task demonstrates a **retrieval-based workflow** combined with **text summarization** using **LangChain** and **Azure OpenAI**.  
It consists of two main components:

1. **`retriever.py`** – Handles document loading, splitting, embedding, and vector-based retrieval.  
2. **`task_3.py`** – Uses the retriever to find relevant text and then summarizes it using the `summary()` function from Task 2.

---

## 🧩 What I Did
- Used LangChain’s **TextLoader** to load a `.txt` file into memory.  
- Split the text into smaller chunks using **RecursiveCharacterTextSplitter** for efficient embedding and retrieval.  
- Generated vector embeddings using **AzureOpenAIEmbeddings**.  
- Stored embeddings in an **InMemoryVectorStore** for fast in-memory retrieval.  
- Queried the retriever with a keyword (“AI Milestones”) to fetch the most relevant text.  
- Passed the retrieved content into the **summary()** function from Task 2 to generate concise summaries.

---

## 💡 What I Understood
- How to use **LangChain retrievers** to find contextually relevant text from a document.  
- How **embeddings** represent text semantically for similarity search.  
- The importance of **text chunking** for better performance and accuracy in retrieval tasks.  
- How to chain multiple LangChain components together — retrieval + summarization — for real-world applications.  
- How to manage Azure OpenAI deployments for both embeddings and chat-based summarization.

---

# 🧠 Task 4 – Creating an Agent for Summarization

This task is part of my **LangChain Training Series**, aimed at understanding how to build autonomous agents that can use tools intelligently to perform summarization tasks.  
The goal was to create an **agent** capable of reasoning about user input and applying a **custom summarization tool** based on the chain built in Task 2.

---

## 📘 Overview

In this task, I designed a system where:
- A **custom LangChain Tool** (`TextSummarizer`) wraps around the summarization chain.
- A **Zero-Shot ReAct Agent** uses this tool to summarize text automatically.
- The agent is tested with both **specific** and **vague** requests to analyze its reasoning process.

This task connects all previous components — environment setup, summarizer chain, and LangChain agent — into one intelligent pipeline.

---

## 🧩 What I Did

- Implemented a function `text_summarizer_tool()` inside **`utils/tools.py`** that transforms the summarization chain into a LangChain-compatible `Tool`.
- Created a `zeroshot_agent()` function inside **`utils/agents.py`** that initializes a **Zero-Shot ReAct agent** using the Azure OpenAI model.
- Developed **`task_4.py`** to:
  - Load environment variables.
  - Initialize the summarization tool and attach it to the agent.
  - Provide a 100-word text about **AI’s impact on healthcare**.
  - Test the agent with:
    1. A clear prompt: “Summarize the impact of AI on healthcare.”
    2. A vague prompt: “Summarize something interesting.”
- Printed both results to compare how the agent responds to specific vs. vague requests.

---

## 💡 What I Understood

- How to create and integrate **custom tools** in LangChain that agents can use automatically.
- The working of **Zero-Shot ReAct Agents**, which can reason about input and decide which tool to call.
- How **LangChain agents** interpret and handle vague instructions using reasoning before taking action.
- The importance of **clear, structured prompts** for consistent and accurate summarization.
- How different LangChain components (LLMs, tools, and environment variables) interact to form a complete intelligent workflow.
- The concept of **ReAct reasoning**, where the agent alternates between *thinking* (reasoning) and *acting* (calling tools).

---

# 🧠 Task 5 – Dynamic Agent with Logging, Exception Handling, and Multiple Tools  

This task builds upon previous LangChain exercises to create a **more robust and dynamic agent pipeline**.  
The objective is to enhance flexibility, debugging, and reliability while integrating multiple tools (retrieval, summarization, and word count) in a single intelligent workflow.  

This task introduces **dynamic configuration**, **file-based logging**, and **structured error handling** to make the agent production-ready.

---

## 📘 Overview  

This project extends the previous tasks by combining all three key components — retrieval, summarization, and analysis — into a single system.  
It dynamically configures tools, initializes a zero-shot agent, executes multiple tasks, and logs every step for traceability.  

The agent can:
- Retrieve text from a document.  
- Summarize it in a defined number of sentences.  
- Optionally count the words in the summary.  

It uses **LangChain exceptions** for structured error handling and Python’s built-in **logging** for file-based debugging.  

---

## 🧩 What I Did  

- Implemented **`configure_tools()`** to dynamically set up all required tools:
  - `retrieval_tool` – extracts relevant document sections.  
  - `text_summarizer_tool` – generates a concise summary.  
  - `word_count_tool` – counts the number of words in the final summary.  
- Built **`create_agent()`** to initialize a **Zero-Shot ReAct agent** using the tools and Azure OpenAI.  
- Added **`execute_agent_tasks()`** to:
  - Run multiple queries dynamically.  
  - Catch and log errors such as parsing issues or runtime failures.  
  - Print cleanly formatted output for each task.  
- Integrated **`langchain_core.exceptions.OutputParserException`** for handling model output parsing errors gracefully.  
- Configured **file-based logging** (`agent_execution.log`) for debugging and process monitoring.  
- Made the system **dynamic** — tool count, file path, and summary length can be changed via parameters.  
- Created and executed two example queries:
  1. Retrieve and summarize details about AI breakthroughs.  
  2. Retrieve, summarize, and count words in the resulting summary.  

---

## 💡 What I Understood  

- How to build **dynamic and reusable LangChain pipelines** that accept parameters instead of hardcoded values.  
- The importance of **structured exception handling** using LangChain’s built-in exception classes.  
- How to implement **file-based logging** to trace agent behavior and diagnose issues without cluttering the terminal.  
- The benefits of combining multiple tools (retriever, summarizer, word counter) into one intelligent agent workflow.  
- The flexibility of the **Zero-Shot ReAct Agent**, which can reason and decide when to use which tool.  
- How well-structured modular functions (`configure_tools`, `create_agent`, `execute_agent_tasks`) improve readability and maintenance.  

---

## ⚙️ Key Features  

| Feature | Description |
|----------|-------------|
| **Dynamic Tool Setup** | Tools are configured based on input parameters with safe defaults. |
| **Logging System** | All operations are recorded in `agent_execution.log` for debugging. |
| **Error Handling** | Uses `OutputParserException` and fallback error handling for unexpected issues. |
| **Multi-Tool Integration** | Combines retrieval, summarization, and word count in one agent. |
| **Configurable Queries** | Supports multiple queries in a single execution cycle. |

---

# 🧠 Task 6 – Context-Aware Summarization with Conversational Memory  

This task is part of my **LangChain Training Series**, focusing on understanding and implementing **conversational memory** within summarization chains.  
The objective was to extend the summarizer created in previous tasks by enabling **context retention** using LangChain’s memory components.

---

## 📘 Overview  

In this task, I modified the existing summarization chain to support two types of conversational memory:

1. **ConversationBufferMemory** – retains the last few interactions exactly as they occurred.  
2. **ConversationSummaryMemory** – maintains a summarized version of prior context to preserve continuity in longer conversations.  

This enhancement enables the summarizer to consider previous user interactions when generating new summaries, creating a more **context-aware** and **stateful** chain.

The task also required comparing how each memory type influences the summarization output and contextual relevance.

---

## 🧩 What I Did  

- Updated the **`summarizer.py`** module to include optional memory support:  
  - Configurable between `"buffer"`, `"summary"`, or `None`.  
  - Defaults to stateless mode for compatibility with earlier tasks.  
  - Integrated **LangChain exceptions** (`OutputParserException`) and file-based logging for debugging.  
- Created **`task_6.py`**, which:  
  - Invokes the updated `summarization_chain()` with both memory types.  
  - Summarizes two related texts:  
    1. A 100-word text about **Machine Learning (ML)**.  
    2. A 100-word text about **Deep Learning (DL)**, while considering the previous summary.  
  - Prints both summaries for comparison.  
- Designed **dynamic defaults** for all configurable parameters (e.g., temperature, number of lines, memory type).  
- Logged all activity to a file for traceability and easier debugging.

---

## 💡 What I Understood  

- **ConversationBufferMemory** keeps the most recent exchanges exactly, making it ideal for **short, detailed** dialogues.  
- **ConversationSummaryMemory** condenses older messages into a **compact summary**, making it more efficient for **longer sessions**.  
- **Context awareness** allows the summarizer to build upon earlier information, producing more coherent results across related inputs.  
- The trade-off: buffer memory preserves details but uses more tokens, while summary memory reduces tokens but may lose fine detail.  
- Integrating memory transforms LangChain chains from **stateless prompt pipelines** into **stateful conversational systems**.  
- Proper **error handling** and **logging** are essential when experimenting with memory-driven workflows.

---

## ⚙️ Key Features  

| Feature | Description |
|----------|-------------|
| **Conversational Memory** | Supports both `ConversationBufferMemory` and `ConversationSummaryMemory`. |
| **Dynamic Defaults** | Parameters such as memory type, lines, and temperature can be adjusted easily. |
| **File-Based Logging** | Records all operations and errors for debugging. |
| **Exception Handling** | Uses LangChain’s `OutputParserException` for structured error capture. |
| **Backward Compatible** | Works with earlier tasks (1–5) when no memory type is provided. |

---

## 🧪 Results & Analysis  

| Memory Type | Behavior | Observed Outcome |
|--------------|-----------|------------------|
| **Buffer** | Keeps last 3 interactions verbatim. | Second summary clearly references and builds on the ML summary. |
| **Summary** | Condenses prior context before reuse. | Second summary is more general, less detailed, but more efficient. |

**Conclusion:**  
- *Buffer Memory* is best for short, detail-rich summarization sessions.  
- *Summary Memory* is better suited for continuous, long-form interactions where token efficiency matters.  

---

# 🧩 Task 7: Leveraging Document Loaders for Diverse Sources

## 📘 Objective
The goal of this task was to **extend document retrieval and summarization capabilities** by incorporating **multiple data source types** — including **text, PDF, and web-based documents**.  
This task demonstrates how LangChain’s document loaders, text splitters, and retrievers can be used dynamically with Azure OpenAI embeddings to extract, process, and summarize information efficiently.

---

## ⚙️ Implementation Details

### 🔹 Files Involved
- `task_7/task7.py` → Main execution file for Task 7.
- `utils/retriever.py` → Enhanced retriever functions to support multi-source loading (text, PDF, web).
- `utils/summarizer.py` → Summarization chain using Azure OpenAI (reused from previous tasks).
- `task_7/AI_Ethics_Report.pdf` → Sample PDF for testing.
- `task_2/task_2.py` → Summary function reused for output display.

---

## 🧠 Workflow Explanation

### 1️⃣ **Loading Documents**
The `text_loader()` function now dynamically selects a loader based on the `path_type` argument:
- `"text"` → Uses `TextLoader` for plain `.txt` files  
- `"pdf"` → Uses `PyPDFLoader` to extract text from PDF documents  
- `"web"` → Uses `WebBaseLoader` to scrape and load web page content  

This makes the system flexible enough to handle multiple content formats without manual intervention.

---

### 2️⃣ **Splitting Documents**
Once loaded, documents are passed to the `text_splitter()` function using `RecursiveCharacterTextSplitter`.  
This ensures:
- Uniform chunk sizes (default `chunk_size=150`)  
- Overlaps of 30 characters to preserve context continuity between chunks.  

---

### 3️⃣ **Creating an In-Memory Vector Store**
The `in_memory_vector_storage()` function:
- Converts text chunks into vector embeddings using **AzureOpenAIEmbeddings**.  
- Stores them in an **InMemoryVectorStore**, enabling semantic retrieval.  
- Returns a retriever that can efficiently find relevant chunks based on a user query.

---

# 🧩 Task 8 – Structured Summarization with JSON Output  

## 📘 Objective  
The objective of Task 8 was to enhance the summarization chain by introducing **structured outputs** using LangChain’s `StructuredOutputParser`.  
Instead of returning plain text, the summarizer now produces **well-formatted JSON responses** that include both the summary and its length, improving readability and enabling easier integration into downstream processes.

---

## ⚙️ Implementation Details  

### 🔹 Files Involved  
- `utils/summarizer.py` → Enhanced to include a `generate_json_summary()` function for structured JSON output.  
- `task_8/task_8.py` → Main driver script that invokes the summarizer and displays formatted JSON results.  

---

## 🧠 Workflow Explanation  

### 1️⃣ **Structured Output Parser Setup**  
The `generate_json_summary()` function defines a **response schema** using LangChain’s `ResponseSchema` objects:
- `"summary"` → Contains the summarized text.  
- `"length"` → Represents the length of the summary in characters.  

A `StructuredOutputParser` is built from these schemas, and its format instructions are embedded into the summarization prompt for the model to follow.

---

### 2️⃣ **Summarization Process**  
The summarization chain from previous tasks (`summarization_chain()`) is reused to generate summaries.  
The model receives both the summarization instruction and JSON formatting rules, ensuring that the response follows the defined schema accurately.

---

### 3️⃣ **Post-Processing and Validation**  
After receiving the model’s raw response:
1. The output is parsed using `parser.parse()`.  
2. The parsed JSON object is printed in a readable format for verification.  

This ensures every summary is **structured, predictable, and machine-readable**.

---

## 🧩 What I Did  
- Enhanced `summarizer.py` to include **StructuredOutputParser** with `ResponseSchema`.  
- Configured dynamic parameters for model temperature, verbosity, and deployment environment variable.  
- Added **file-based logging** for debugging and transparency.  
- Implemented **`generate_json_summary()`** to return:
  - A properly configured LLM instance.  
  - A structured output parser.  
  - The formatting instructions required for JSON generation.  
- Created **`task_8.py`** to:
  - Provide a 150-word passage about AI applications.  
  - Request a structured summary in JSON format.  
  - Parse and display the result.

---

## 💡 What I Understood  
- How to use **LangChain’s StructuredOutputParser** for structured JSON-based model responses.  
- The significance of defining **response schemas** for predictable and validated LLM outputs.  
- How structured responses improve **automation**, **evaluation**, and **integration** of AI-generated content.  
- How to maintain both **human readability** and **programmatic consistency** in summarization pipelines.  

---

## ⚙️ Key Features  

| Feature | Description |
|----------|-------------|
| **Structured Output Parser** | Ensures the model generates valid JSON responses. |
| **Response Schemas** | Defines consistent fields for output data. |
| **Dynamic Model Configuration** | Flexible setup for temperature and environment variables. |
| **File-Based Logging** | Records key operations and parsing activities. |
| **JSON-Formatted Summaries** | Returns both the summary and its length in structured form. |

---

# 🧩 Task 9 – Experimenting with Multi-Query Retrieval  

## 📘 Objective  
The objective of Task 9 was to explore **multi-query retrieval** techniques using LangChain’s `MultiQueryRetriever`.  
This experiment extends the standard retriever-based pipeline by generating multiple semantically diverse queries to improve retrieval accuracy and coverage from the same knowledge base.

---

## ⚙️ Implementation Details  

### 🔹 Files Involved  
- `task_9/task_9.py` → Main driver script for single-query vs. multi-query comparison.  
- `utils/retriever.py` → Enhanced with a new `multi_query()` function for dynamic multi-query retrieval.  
- `utils/summarizer.py` → Used to summarize retrieved content through the `summarization_chain()` function from earlier tasks.  

---

## 🧠 Workflow Explanation  

### 1️⃣ **Single-Query Retrieval**  
The process begins by loading a text file (`ai_intro.txt`) and preparing it for vector storage using:
- `text_loader()` to load the document.  
- `text_splitter()` to chunk the text into segments.  
- `in_memory_vector_storage()` to create an in-memory vector retriever using **Azure OpenAI Embeddings**.  

A single query (e.g., `"AI advancements"`) is used to retrieve relevant chunks, which are then summarized using the summarization chain.

---

### 2️⃣ **Multi-Query Retrieval**  
Next, the **MultiQueryRetriever** is introduced:
- Uses the same base retriever and embeddings.  
- Employs `AzureChatOpenAI` as the LLM to generate **multiple rephrased queries** of the same intent.  
- Each generated query retrieves potentially different relevant text segments, improving diversity and recall.  

These retrieved chunks are merged and summarized collectively, producing a more comprehensive summary.

---

### 3️⃣ **Query Generation & Comparison**  
For a fair comparison:
- The **single-query retriever** retrieves text for `"AI advancements"` directly.  
- The **multi-query retriever** automatically expands that query into multiple paraphrased forms (e.g., “recent AI developments,” “AI progress milestones,” etc.).  
- Both retrieved sets are summarized using the same `summarization_chain()` for consistency.  

This allows side-by-side observation of how multi-query retrieval improves coverage and depth.

---

## 🧩 What I Did  
- Integrated `MultiQueryRetriever` from LangChain into the retrieval pipeline.  
- Implemented a `multi_query()` function in `retriever.py` that:  
  - Loads and splits text documents.  
  - Creates an in-memory vector retriever.  
  - Wraps it with a **multi-query retriever** powered by `AzureChatOpenAI`.  
- Enhanced `task_9.py` to:  
  - Compare single-query and multi-query summaries.  
  - Print generated alternate queries and retrieved chunks for transparency.  
  - Summarize both retrieval outputs using the existing summarization chain.  

---

## 💡 What I Understood  
- How **multi-query retrieval** expands a single query into multiple reformulations to capture semantically diverse information.  
- The role of **LLMs in query expansion**, making retrieval more robust across varied phrasing.  
- How combining multiple retrievals enhances **recall** while maintaining relevance.  
- The importance of **consistent summarization** to fairly compare retrieval performance.  
- How LangChain’s modular retriever design enables rapid experimentation across retrieval strategies.  

---

## ⚙️ Key Features  

| Feature | Description |
|----------|-------------|
| **MultiQueryRetriever Integration** | Uses an LLM to generate alternate query phrasings automatically. |
| **Single vs Multi Query Comparison** | Demonstrates retrieval diversity and summarization improvement. |
| **Dynamic Chunking and Embedding** | Maintains consistent document preprocessing for fair testing. |
| **Azure Integration** | Uses Azure OpenAI for both embeddings and LLM-based query generation. |
| **Detailed Console Output** | Displays generated queries, retrieved chunks, and summaries for analysis. |

---

