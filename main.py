from dotenv import load_dotenv
load_dotenv()

import os
from utils.job_scraper import get_mock_jobs
from utils.ai_filter import filter_jobs
from utils.email_sender import output_html

RESUME_PATH = "resume.txt"

def load_resume(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def main():
    resume = load_resume(RESUME_PATH)
    jobs = get_mock_jobs()
    relevant_jobs = filter_jobs(resume, jobs)
    output_html(relevant_jobs)

if __name__ == "__main__":
    main()