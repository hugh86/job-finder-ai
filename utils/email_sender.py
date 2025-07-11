import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def output_html(jobs, filename="output/job_matches.html"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("<html><body><h2>Matching Jobs</h2><ul>")
        for job in jobs:
            f.write(f"<li><strong>{job['title']}</strong><br>{job['description']}<br><em>{job.get('reason', '')}</em></li><br>")
        f.write("</ul></body></html>")

def send_email_with_html_file(to_email, subject, html_file):
    from_email = os.getenv("EMAIL_SENDER")
    app_password = os.getenv("EMAIL_APP_PASSWORD")

    # Read HTML content
    with open(html_file, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Compose email
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email
    part = MIMEText(html_content, "html")
    msg.attach(part)

    # Send email via Gmail SMTP
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(from_email, app_password)
        server.sendmail(from_email, to_email, msg.as_string())
        print("📧 Email sent!")
