import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: open website
url = "http://quotes.toscrape.com"
response = requests.get(url)

# Step 2: read website content
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: create empty lists
quotes = []
authors = []
tags = []

# Step 4: find data
for item in soup.find_all("div", class_="quote"):
    quotes.append(item.find("span", class_="text").text)
    authors.append(item.find("small", class_="author").text)
    tags.append(", ".join([tag.text for tag in item.find_all("a", class_="tag")]))

# Step 5: create table
df = pd.DataFrame({
    "Quote": quotes,
    "Author": authors,
    "Tags": tags
})

# Step 6: save to file
df.to_csv("quotes.csv", index=False)

print("✅ Data saved to quotes.csv")