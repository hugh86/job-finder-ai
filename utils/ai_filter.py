import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def filter_jobs(resume, jobs):
    relevant = []
    for job in jobs:
        prompt = f"Resume:\n{resume}\n\nJob Posting:\nTitle: {job['title']}\nDescription: {job['description']}\n\nIs this job a good fit for the candidate based on the resume? Answer yes or no, and explain why."
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}]
            )
            answer = response['choices'][0]['message']['content']
            if "yes" in answer.lower():
                job["reason"] = answer.strip()
                relevant.append(job)
        except Exception as e:
            print("Error with OpenAI API:", e)
    return relevant