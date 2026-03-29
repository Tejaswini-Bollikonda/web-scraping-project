import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Open website
base_url = "https://realpython.github.io/fake-jobs/"
jobs = []

for page in range(1, 6):  
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


# Step 2: Save to CSV
df = pd.DataFrame(jobs)
df.to_csv("jobs.csv", index=False)

# Step 3: Smarter filtering (FINAL FIXED)

keywords = [
    "python developer",
    "software engineer",
    "data scientist",
    "data engineer",
    "machine learning",
    "artificial intelligence"
]

pattern = "|".join(keywords)   # ← remove regex complexity

filtered_jobs = df[df["Title"].str.lower().str.contains(pattern, na=False)]

filtered_jobs = filtered_jobs.drop_duplicates(subset=["Title", "Company"])
filtered_jobs.to_csv("filtered_jobs.csv", index=False)

print("Filtered jobs saved!")

