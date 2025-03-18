Job Search API
This is a FastAPI-based application that aggregates job listings from multiple sources, including APIs (Upwork, Remote Jobs, Glassdoor, Freelancer, Indeed, LinkedIn) and web scraping (Rozee.pk, Naukri.com). It filters results using a Hugging Face sentiment analysis model to ensure relevance based on user-defined criteria.

Project Structure

job-search-api/
├── main.py          # FastAPI app and endpoint definition
├── model.py         # Pydantic model for job search criteria
├── job_api.py       # API integration functions for job platforms
├── job_scraping.py  # Web scraping functions for job sites
├── utils.py         # Utility functions (e.g., job filtering with Hugging Face)

Features
API Integrations: Fetches jobs from Upwork, Remote Jobs, Glassdoor, Freelancer, Indeed, and LinkedIn using RapidAPI endpoints.
Web Scraping: Scrapes job listings from Rozee.pk and Naukri.com using requests and BeautifulSoup.
Relevance Filtering: Uses a Hugging Face sentiment analysis model to filter jobs based on user criteria.
Modular Design: Code is split into separate files for models, APIs, scraping, and utilities.

Prerequisites
Python 3.8+
Required Python libraries:
fastapi
uvicorn
requests
beautifulsoup4
transformers
torch


Setup
  Clone the Repository:
    Download or clone this project to your local machine.
  Install Dependencies:
    Open a terminal in the project directory and install the required Python libraries using pip:
      Command: pip install fastapi uvicorn requests beautifulsoup4 transformers torch
  Verify RapidAPI Key:
    Ensure the x-rapidapi-key in job_api.py (d4c93ae110msh088723deafe6d9bp152adajsn07e8e81bd899) is valid. Replace it with your own RapidAPI key if necessary.

Running the Application
  Start the Server:
    In the project directory, run the FastAPI application using uvicorn:
      Command: uvicorn main:app --reload
    The --reload flag enables auto-reloading for development.
  Access the API:
    The API will be available at http://127.0.0.1:8000.

Usage
Endpoint: /find-jobs
Method: POST
Request Body: JSON object with the following fields (based on JobSearchCriteria model):
  position (str, required): Job title or keyword (e.g., "data engineer").
  location (str, required): Job location (e.g., "remote", "New York, USA").
  experience (str, optional): Desired experience level (e.g., "1 years").
  salary (str, optional): Desired salary (e.g., "50,000 PKR").
  jobNature (str, optional): Job type (e.g., "fulltime").
  skills (str, optional): Required skills (e.g., "Python, SQL").

Example Request:
    import requests

    url = "http://127.0.0.1:8000/find-jobs"
    data = {
        "position": "data engineer",
        "location": "remote",
        "experience": "1 years",
        "salary": "50,000 PKR",
        "jobNature": "fulltime",
        "skills": "Python, SQL"
    }
    response = requests.post(url, json=data)
    print(response.json())

Response:
A JSON object with a "relevant_jobs" key containing a list of job dictionaries.
Each job includes:
job_title: Job title.
company: Company name.
experience: Experience level (from source or criteria).
jobNature: Job type (from source or criteria).
location: Requested location.
salary: Salary (from source or criteria).
apply_link: URL to apply for the job.
Example Response:

  {
      "relevant_jobs": [
          {
              "job_title": "Data Engineer",
              "company": "Tech Corp",
              "experience": "1 years",
              "jobNature": "fulltime",
              "location": "remote",
              "salary": "50,000 PKR",
              "apply_link": "https://example.com/job/123"
          }
      ]
  }
Notes
RapidAPI Key: The provided key is for demonstration. Replace it with your own from RapidAPI if you encounter quota issues or errors.
Scraping Limitations: Rozee.pk and Naukri.com scraping may fail due to anti-scraping measures (e.g., 403 Forbidden). Consider using Selenium (not included here) for more robust scraping.
API Rate Limits: RapidAPI free tiers have limits (e.g., 100 requests/month). Monitor usage or upgrade your plan for production use.
Error Handling: Check console logs for errors (e.g., "Error fetching jobs from [source]") to debug issues.
Performance: The application fetches and filters jobs synchronously. For large-scale use, consider async implementations.
Contributing
Feel free to fork this project, submit pull requests, or open issues for improvements or bug fixes.

License
This project is unlicensed and free to use as a starting point for your own applications.