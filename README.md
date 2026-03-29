Version: v2 (Multi-page scraping + filtering + job links)

# Web Scraping Project (Python)

## Overview

This project is a Python-based web scraper that extracts job data from a website and stores it in a structured format (CSV).

It collects job titles, company names, locations, and links, and filters relevant roles like Python, Data, AI, and related fields.

This project simulates a real-world data pipeline:
**Extract → Filter → Store**

---

## Features

* Scrapes job data from a live website
* Supports multi-page scraping (pagination)
* Extracts:

  * Job Title
  * Company
  * Location
  * Job Link
* Filters relevant jobs (Python, Data, AI, etc.)
* Removes duplicate entries
* Saves clean structured data in CSV format

---

## Tech Stack

* Python
* Requests
* BeautifulSoup
* Pandas

---

## Project Flow (Step-by-Step)

1. Send request to website using `requests`
2. Parse HTML using `BeautifulSoup`
3. Extract job data (title, company, location, link)
4. Loop through multiple pages (pagination)
5. Store data into a Pandas DataFrame
6. Apply filtering based on keywords
7. Remove duplicate jobs
8. Save output into CSV files

---

## How to Run (Beginner Friendly)

### Step 1: Install dependencies

```bash or cmd
pip install requests beautifulsoup4 pandas
```

### Step 2: Run the script

```bash or cmd
python job_scraper.py
```

---

## Output Files

* `jobs.csv` → All scraped jobs
* `filtered_jobs.csv` → Only relevant jobs (Python, Data, AI, etc.)

---

## Example Output

| Title                   | Company | Location | Link        |
| ----------------------- | ------- | -------- | ----------- |
| Senior Python Developer | XYZ     | USA      | https://... |

---

## Key Learnings

* Web scraping using BeautifulSoup
* Handling real-world HTML data
* Data cleaning & filtering using Pandas
* Building a simple data pipeline
* Working with CSV datasets
* Debugging and fixing errors (permissions, duplicates, etc.)

---

## Current Version

### v1

* Basic scraping
* Single page extraction
* CSV output

### v2 (Current)

* Multi-page scraping (pagination)
* Keyword-based filtering
* Duplicate removal
* Job links added

---

## Next Improvements

* Add delay (avoid blocking)
* Add error handling (try/except)
* Sort jobs (latest first)
* Store data in database (SQL)
* Automate pipeline

---

## Author

Tejaswini Bollikonda
