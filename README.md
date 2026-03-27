Version: v1 (Basic scraper with filtering & links)

# Web Scraping Project (Python)

## Overview
I built a Python-based web scraper that extracts data from a website and stores it in a structured format for analysis.
The script collects quotes, authors, and tags from single or multiple pages and saves the data into a CSV file.

---

## Features
- Scrapes data from a live website
- Supports multi-page scraping
- Extracts quotes, authors, and tags
- Stores structured data in CSV format
- Performs basic data analysis using Pandas

---

## Tech Stack
- Python
- Requests
- BeautifulSoup
- Pandas

---

## How It Works
1. Sends a request to the website using `requests`
2. Parses HTML content using `BeautifulSoup`
3. Extracts quotes, authors, and tags
4. Loops through multiple pages to collect more data(after upgrade)
5. Stores the extracted data into a Pandas DataFrame
6. Saves the data into a CSV file

---

## How to Run

1. Install dependencies:
pip install requests beautifulsoup4 pandas

2. Run the script:
python scraper.py

---

## Output
- quotes.csv → data from single page  
- quotes_all_pages.csv → data from multiple pages(after upgrade)  

---

## What I Learned
- How to extract real-world data from websites
- Understanding HTML structure
- Building a simple data pipeline (extract → transform → load)
- Debugging environment issues

---

## Next Steps
- Build job scraping project (Indeed/LinkedIn style)
- Store data in SQL database
- Automate the pipeline

---

## Author
Tejaswini Bollikonda
