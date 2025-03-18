from transformers import pipeline

# Initialize Hugging Face model for relevance filtering
relevance_classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def filter_jobs_with_huggingface(criteria, jobs: list) -> list:
    criteria_text = f"Job title: {criteria.position}, Location: {criteria.location}, Skills: {criteria.skills or 'N/A'}, Experience: {criteria.experience or 'N/A'}, Salary: {criteria.salary or 'N/A'}, Job Nature: {criteria.jobNature or 'N/A'}"
    relevant_jobs = []
    for job in jobs:
        job_text = f"Job title: {job['title']}, Description: {job['description']}, Company: {job['company']}, Job Type: {job['job_type']}"
        result = relevance_classifier(f"Is this job relevant to the following criteria? Criteria: {criteria_text}. Job: {job_text}")[0]
        if result["label"] == "POSITIVE" and result["score"] > 0.4:
            relevant_jobs.append(job)
    print(f"Filtered to {len(relevant_jobs)} relevant jobs")
    return relevant_jobs