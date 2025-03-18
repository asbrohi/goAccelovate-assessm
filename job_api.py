import requests

# API headers (using a single RapidAPI key for simplicity)
API_HEADERS = {
    "x-rapidapi-key": "d4c93ae110msh088723deafe6d9bp152adajsn07e8e81bd899",
}

def search_remote_jobs(criteria) -> list:
    url = "https://remote-jobs1.p.rapidapi.com/jobs"
    if criteria.location.lower() == "remote":
        querystring = {"offset": "0", "employmentType": criteria.jobNature or "fulltime"}
    else:
        country = criteria.location.split(",")[-1].strip()
        querystring = {"offset": "0", "country": country, "employmentType": criteria.jobNature or "fulltime"}
    headers = {**API_HEADERS, "x-rapidapi-host": "remote-jobs1.p.rapidapi.com"}
    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        raw_data = response.json()
        print(f"Remote Jobs raw response: {raw_data}")
        
        if isinstance(raw_data, list):
            jobs = raw_data
        else:
            jobs = raw_data.get("data", [])
        
        print(f"Remote Jobs fetched {len(jobs)} jobs")
        return [
            {
                "title": job.get("title", "N/A"),
                "company": job.get("company_name", "N/A"),
                "link": job.get("url", ""),
                "description": job.get("description", "N/A"),
                "salary": job.get("salary", "N/A"),
                "experience": job.get("experience", "N/A"),
                "job_type": job.get("employment_type", "N/A")
            }
            for job in jobs
        ]
    except requests.RequestException as e:
        print(f"Error fetching jobs from Remote Jobs: {e}")
        return []

def search_glassdoor(criteria) -> list:
    url = "https://glassdoor-real-time.p.rapidapi.com/search/job"
    querystring = {
        "keyword": criteria.position,
        "location": criteria.location,
        "page": "1"
    }
    headers = {**API_HEADERS, "x-rapidapi-host": "glassdoor-real-time.p.rapidapi.com"}
    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        raw_data = response.json()
        print(f"Glassdoor raw response: {raw_data}")
        jobs = raw_data.get("data", {}).get("jobListings", [])
        print(f"Glassdoor fetched {len(jobs)} jobs")
        return [
            {
                "title": job.get("jobTitleText", "N/A"),
                "company": job.get("employer", {}).get("name", "N/A"),
                "link": job.get("jobViewUrl", ""),
                "description": job.get("description", "N/A"),
                "salary": job.get("payPeriodAdjustedPay", {}).get("p50", "N/A"),
                "experience": "N/A",
                "job_type": job.get("jobType", "N/A")
            }
            for job in jobs
        ]
    except requests.RequestException as e:
        print(f"Error fetching jobs from Glassdoor: {e}")
        return []

def search_indeed(criteria) -> list:
    url = "https://indeed12.p.rapidapi.com/jobs/search"
    querystring = {
        "query": criteria.position,
        "location": criteria.location if criteria.location.lower() != "remote" else "remote",
        "page_id": "1",
        "locality": "us" if criteria.location.lower() == "remote" else criteria.location.split(",")[-1].strip().lower(),
        "sort_by": "relevance"
    }
    headers = {**API_HEADERS, "x-rapidapi-host": "indeed12.p.rapidapi.com"}
    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        raw_data = response.json()
        print(f"Indeed raw response: {raw_data}")
        jobs = raw_data.get("hits", [])
        print(f"Indeed fetched {len(jobs)} jobs")
        return [
            {
                "title": job.get("title", "N/A"),
                "company": job.get("company_name", "N/A"),
                "link": f"https://www.indeed.com/viewjob?jk={job.get('jobkey', '')}",
                "description": job.get("description", "N/A"),
                "salary": job.get("salary", {}).get("max", "N/A"),
                "experience": "N/A",
                "job_type": job.get("type", "N/A")
            }
            for job in jobs
        ]
    except requests.RequestException as e:
        print(f"Error fetching jobs from Indeed: {e}")
        return []

def search_linkedin(criteria) -> list:
    url = "https://linkedin-jobs-search.p.rapidapi.com/"
    payload = {
        "search_terms": criteria.position,
        "location": criteria.location if criteria.location.lower() != "remote" else "Remote",
        "page": "1"
    }
    headers = {
        **API_HEADERS,
        "x-rapidapi-host": "linkedin-jobs-search.p.rapidapi.com",
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        raw_data = response.json()
        print(f"LinkedIn raw response: {raw_data}")
        jobs = raw_data if isinstance(raw_data, list) else raw_data.get("data", [])
        print(f"LinkedIn fetched {len(jobs)} jobs")
        return [
            {
                "title": job.get("job_title", "N/A"),
                "company": job.get("company_name", "N/A"),
                "link": job.get("linkedin_job_url", ""),
                "description": job.get("job_description", "N/A"),
                "salary": "N/A",
                "experience": "N/A",
                "job_type": job.get("employment_type", "N/A")
            }
            for job in jobs
        ]
    except requests.RequestException as e:
        print(f"Error fetching jobs from LinkedIn: {e}")
        return []