from utils.summarizer import summarization_chain

def main(memory_type:str):
    chain=summarization_chain(memory_type=memory_type,lines=3)
    
    ml_text = """
Machine learning (ML) is a branch of artificial intelligence that enables computers to learn from data
and improve automatically through experience. Instead of being explicitly programmed, ML models identify
patterns and make predictions or decisions based on historical information. Supervised learning uses labeled
data to train algorithms, while unsupervised learning discovers hidden structures within datasets.
Reinforcement learning helps systems adapt through rewards and penalties. Machine learning powers applications
such as spam filtering, speech recognition, recommendation systems, and fraud detection, transforming industries
by enabling smarter automation, data-driven insights, and continuous performance improvement.
"""
    output=chain.invoke(
        {"text":ml_text}
    )
    print("Machine Learning Summary",output)
    dl_text = """
Deep learning (DL) is an advanced subset of machine learning that uses artificial neural networks
with multiple layers to process and learn from complex data. Inspired by the structure of the human brain,
deep learning models automatically extract features from large datasets without manual intervention.
They excel in areas such as computer vision, speech recognition, and natural language processing.
By leveraging vast computing power and massive amounts of data, DL systems achieve exceptional accuracy
in tasks like image classification, autonomous driving, and medical diagnostics, revolutionizing technology
through intelligent automation, data-driven understanding, and continuous improvement across diverse applications.
"""
    output=chain.invoke(
        {"text":dl_text}
    )
    print("Deep Learning Summary considering prior summary",output)

if __name__=="__main__":
    print("================== RUNNING TASK 6 ==================")
    main("buffer")
    main("Summary")