Version: v4 (Error handling + safe scraping + improved filtering)
Version: v3 (Improved filtering logic + keyword matching)
Version: v2 (Multi-page scraping + filtering + job links)
Version: v1 (Basic singscraper with filtering)


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
* Smart keyword-based filtering (v3 improved logic) (Python, Data, AI, etc.)
* Removes duplicate entries
* Error handling (prevents crashes)
* Safe scraping (handles failed requests/pages)
* Delay between requests (avoids blocking)
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
6. Apply keyword-based filtering
7. Remove duplicate jobs
8. Handle errors safely using `try/except`  
9. Add delay between requests to avoid blocking
10. Save output into CSV files

---

## How to Run

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

## Current Version

### v1

* Basic scraping
* Single page extraction
* CSV output

### v2 

* Multi-page scraping (pagination)
* Keyword-based filtering
* Duplicate removal
* Job links added

### v3
* Improved filtering logic
* Better keyword matching
* Cleaner and more accurate results

### v4(Current)
Error handling with try/except
Safe request handling
Skips failed pages/jobs instead of crashing
Delay added to avoid blocking
More stable and production-like scraper

---

## Next Improvements

* Add job scoring (better relevance ranking)
* Sort jobs (latest first)
* Store data in database (SQL)
* Automate pipeline (scheduler)
* Deploy as a service


