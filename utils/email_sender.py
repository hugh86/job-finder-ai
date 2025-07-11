def output_html(jobs, filename="job_matches.html"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("<html><body><h2>Matching Jobs</h2><ul>")
        for job in jobs:
            f.write(f"<li><strong>{job['title']}</strong><br>{job['description']}<br><em>{job.get('reason', '')}</em></li><br>")
        f.write("</ul></body></html>")