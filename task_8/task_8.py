import json
from utils.summarizer import generate_json_summary

def main():
    llm,parser,format_instructions=generate_json_summary(lines=3)
    
    text = """
Artificial Intelligence (AI) continues to reshape industries through automation, data analysis,
and decision-making capabilities. In healthcare, it enables precise diagnostics and predictive
treatments. In finance, AI supports fraud detection and market forecasting. The education sector
benefits from adaptive learning platforms that personalize teaching. Transportation uses AI for
autonomous driving and efficient route management. Despite immense benefits, AI raises concerns
about job displacement, bias, and data security. Addressing these challenges while ensuring
ethical deployment is essential for sustainable technological growth.
"""
    json_prompt = (
        f"Summarize the passage below into exactly 3 sentences.\n\n"
        f"Follow these format instructions:\n{format_instructions}\n\n"
        f"Passage:\n{text}"
    )
    
    llm_response = llm.invoke(json_prompt)
    # Step 5: Parse and enrich the result
    parsed_output = parser.parse(llm_response.content)
    parsed_output["length"] = len(parsed_output["summary"])

    result_json = json.dumps(parsed_output, indent=4)
    print("--- Structured JSON Output ---\n", result_json)



if __name__ == "__main__":
    print("================== RUNNING TASK 8 ==================")
    main()