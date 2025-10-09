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
