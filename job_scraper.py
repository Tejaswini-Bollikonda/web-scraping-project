import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Step 1: Smarter filtering (FINAL FIXED)
relevant_roles = [
    "python",
    "genai",
    "software engineer",
    "data scientist",
    "data engineer",
    "analytics",
    "aiml",
    "devops",
    "servicenow",
    "frontend",
    "backend"
]

def is_relevant(title):
    title = title.lower()
    return any(role in title for role in relevant_roles)



# Step 2: Open website
base_url = "https://realpython.github.io/fake-jobs/"
jobs = []

for page in range(1, 6):  # change to x later
    if page == 1:
        url = base_url
    else:
        url = f"{base_url}page/{page}/"
    print(f"Scraping page {page}...")

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    for job in soup.find_all("div", class_="card-content"):
        title = job.find("h2", class_="title").text.strip()
        company = job.find("h3", class_="company").text.strip()
        location = job.find("p", class_="location").text.strip()
        link = job.find("a")["href"]

        jobs.append({
            "Title": title,
            "Company": company,
            "Location": location,
            "Link": link
        })


# Step 3: Save to CSV
df = pd.DataFrame(jobs)
df.to_csv("jobs.csv", index=False)


# 👉 FIRST create filtered_jobs
filtered_jobs = df[df["Title"].apply(is_relevant)]
filtered_jobs = filtered_jobs.copy()

# Step 4: Remove duplicates
filtered_jobs = filtered_jobs.drop_duplicates(subset=["Title", "Company", "Location"])

# Step 5: Ranking (score)
priority_keywords = ["python", "ai", "machine learning", "data"]

def score_job(title):
    title = title.lower()
    return sum(1 for word in priority_keywords if word in title)

filtered_jobs["score"] = filtered_jobs["Title"].apply(score_job)

# Step 6: Sort
filtered_jobs = filtered_jobs.sort_values(by="score", ascending=False)

# Step 7: Reset index
filtered_jobs = filtered_jobs.reset_index(drop=True)
filtered_jobs.to_csv("filtered_jobs.csv", index=False)

print("Filtered jobs saved!")


