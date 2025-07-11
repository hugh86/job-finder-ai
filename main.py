import os
from dotenv import load_dotenv
from utils.job_scraper import get_mock_jobs
from utils.ai_filter import filter_jobs
from utils.email_sender import output_html, send_email_with_html_file

# Load environment variables from .env file
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

    # Load output path from .env
    output_path = os.getenv("HTML_OUTPUT_PATH", "output/job_matches.html")

    # Save HTML report
    output_html(relevant_jobs, filename=output_path)
    print(f"📄 Report saved to {output_path}")

    # Email the report
    send_email_with_html_file(
        to_email=os.getenv("EMAIL_TO"),
        subject=os.getenv("EMAIL_SUBJECT", "Your AI-Filtered Job Matches"),
        html_file=output_path
    )

if __name__ == "__main__":
    main()
