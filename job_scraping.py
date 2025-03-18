import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://www.google.com/",
    "DNT": "1",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
}

def scrape_rozee_pk(position: str, location: str) -> list:
    city = location.split(",")[0].strip().lower().replace(" ", "-")
    url = f"https://www.rozee.pk/jobs-in-{city}"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = []
        for job in soup.select(".job"):
            title = job.select_one(".jobtitle")
            company = job.select_one(".company")
            link = job.select_one("a")
            jobs.append({
                "title": title.text.strip() if title else "N/A",
                "company": company.text.strip() if company else "N/A",
                "link": "https://www.rozee.pk" + link["href"] if link else "",
                "description": "N/A",
                "salary": "N/A",
                "experience": "N/A",
                "job_type": "N/A"
            })
        print(f"Rozee.pk fetched {len(jobs)} jobs")
        return jobs
    except requests.RequestException as e:
        print(f"Error scraping Rozee.pk: {e}")
        return []

def scrape_naukri(position: str, location: str) -> list:
    city = location.split(",")[0].strip().lower().replace(" ", "-")
    url = f"https://www.naukri.com/{position.lower().replace(' ', '-')}-jobs-in-{city}"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = []
        for job in soup.select(".jobTuple"):
            title = job.select_one(".title")
            company = job.select_one(".companyName")
            link = job.select_one("a")
            jobs.append({
                "title": title.text.strip() if title else "N/A",
                "company": company.text.strip() if company else "N/A",
                "link": link["href"] if link else "",
                "description": "N/A",
                "salary": "N/A",
                "experience": "N/A",
                "job_type": "N/A"
            })
        print(f"Naukri fetched {len(jobs)} jobs")
        return jobs
    except requests.RequestException as e:
        print(f"Error scraping Naukri: {e}")
        return []