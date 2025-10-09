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
