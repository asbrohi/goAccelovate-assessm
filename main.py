from fastapi import FastAPI
from model import JobSearchCriteria
from job_api import search_upwork, search_remote_jobs, search_glassdoor, search_freelancer, search_indeed, search_linkedin
from job_scraping import scrape_rozee_pk, scrape_naukri
from utils import filter_jobs_with_huggingface 

# Initialize FastAPI app
app = FastAPI()

@app.post("/find-jobs")
async def find_jobs(criteria: JobSearchCriteria):
    position = criteria.position
    location = criteria.location

    # Collect jobs from all sources
    all_jobs = []
    all_jobs.extend(search_remote_jobs(criteria))
    all_jobs.extend(search_glassdoor(criteria))
    all_jobs.extend(search_indeed(criteria))
    all_jobs.extend(search_linkedin(criteria))
    all_jobs.extend(scrape_rozee_pk(position, location))
    all_jobs.extend(scrape_naukri(position, location))

    # Filter jobs
    relevant_jobs = filter_jobs_with_huggingface(criteria, all_jobs)

    # Structure the response
    output_jobs = [
        {
            "job_title": job["title"],
            "company": job["company"],
            "experience": job["experience"] if job["experience"] != "N/A" else criteria.experience or "N/A",
            "jobNature": job["job_type"] if job["job_type"] != "N/A" else criteria.jobNature or "N/A",
            "location": location,
            "salary": job["salary"] if job["salary"] != "N/A" else criteria.salary or "N/A",
            "apply_link": job["link"]
        }
        for job in relevant_jobs
    ]

    print(f"Returning {len(output_jobs)} jobs")
    return {"relevant_jobs": output_jobs}

