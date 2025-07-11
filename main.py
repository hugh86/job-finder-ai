import os
from dotenv import load_dotenv
from utils.job_scraper import get_mock_jobs
from utils.ai_filter import filter_jobs
from utils.email_sender import output_html

# Load .env variables
load_dotenv()

RESUME_PATH = "resume.txt"

def load_resume(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def main():
    print("📄 Loading resume...")
    resume = load_resume(RESUME_PATH)

    print("🔎 Fetching jobs...")
    jobs = get_mock_jobs()

    print("🧠 Filtering with GPT...")
    relevant_jobs = filter_jobs(resume, jobs)

    print(f"✅ Found {len(relevant_jobs)} relevant jobs.")
    output_html(relevant_jobs)
    print("📬 Results saved to job_matches.html")

if __name__ == "__main__":
    main()