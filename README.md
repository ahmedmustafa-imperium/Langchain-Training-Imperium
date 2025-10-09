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

