import requests

url = "http://127.0.0.1:8000/find-jobs"
data = {
    "position": "software engineer",
    "location": "karachi",
    "experience": "3 years",
    "salary": "120000",
    "jobNature": "full_time",
    "skills": "python, javascript"
}
response = requests.post(url, json=data)
print(response.json())