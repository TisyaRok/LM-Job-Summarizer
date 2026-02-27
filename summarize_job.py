import os
from google import genai

def load_job_description(filepath):
    with open(filepath, "r") as f:
        return f.read()

def summarize_skills(job_description):
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    
    # Using the current 2026 stable model ID
    model_id = "gemini-2.5-flash" 
    
    prompt = f"""Read the following job description and summarize it into exactly 5 key skill requirements.
Format your response as a numbered list.
Job Description:
{job_description}"""

    response = client.models.generate_content(
        model=model_id,
        contents=prompt
    )
    return response.text
def main():
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(script_dir, "job_description.txt")
        job_description = load_job_description(filepath)
        skills = summarize_skills(job_description)
        print("Top 5 Key Skills:\n")
        print(skills)
    except FileNotFoundError:
        print("Error: job_description.txt not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()