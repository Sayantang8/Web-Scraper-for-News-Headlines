import requests
from bs4 import BeautifulSoup
import os

headers = {
    "User-Agent": "Mozilla/5.0" # Part of the User-Agent header to trick the website into thinking the request is coming from a real browser, not a Python script.


}
url = "https://timesofindia.indiatimes.com" # Using the Times of India website.
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Extract headlines
headline_tags = soup.find_all("a")
headlines = []
for tag in headline_tags:
    text = tag.get_text(strip=True)
    if text and len(text.split()) > 4:
        headlines.append(text)

# Save file on Desktop
file_path = os.path.join(os.path.expanduser("~"), "Desktop", "headlines.txt")

if headlines:
    with open(file_path, "w", encoding="utf-8") as f:
        for index, headline in enumerate(headlines, 1): # Start enumeration from 1
            # Write each headline with its index
            f.write(f"{index}. {headline}\n")
    print(f" File saved to: {file_path}")

    # Automatically open the file (Windows only)
    os.startfile(file_path)
else:
    print(" No headlines found.")
