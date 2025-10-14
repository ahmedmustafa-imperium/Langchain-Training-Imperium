
from utils.summarizer import summarization_chain
def summary(text: str):


    summarizer=summarization_chain(lines=3)
    summary_3=summarizer.invoke({"text": text}).content
    print("3 lines Summary\n",summary_3)
    
    summarizer=summarization_chain(lines=1)
    summary_1=summarizer.invoke({"text": text}).content
    print("\n\n 1 lines Summary\n",summary_1)

if __name__=="__main__":
    print("================== RUNNING TASK 2 ==================")
    text = """
Artificial Intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think, learn, and make decisions. 
Over the past few decades, AI has evolved from simple rule-based systems to advanced models capable of perception, reasoning, and language understanding. 
Machine learning, a subset of AI, allows systems to improve their performance automatically through data-driven learning. 
Deep learning, which uses neural networks, has further accelerated AI's progress in image recognition, natural language processing, and autonomous systems. 
AI applications are now widespread, influencing industries such as healthcare, finance, manufacturing, and transportation. 
In healthcare, AI assists in diagnosing diseases, analyzing medical images, and predicting patient outcomes. 
In finance, algorithms detect fraud and optimize trading strategies. 
Despite its advantages, AI raises ethical concerns related to bias, job displacement, and data privacy. 
As AI becomes increasingly integrated into society, researchers emphasize the importance of transparency, fairness, and accountability in AI systems. 
The future of AI lies in developing more explainable, secure, and general-purpose systems that can collaborate effectively with humans while preserving trust and ethical integrity. 
Ultimately, AI represents both an opportunity and a challenge, shaping the next era of technological and societal transformation.
"""
    summary(text)