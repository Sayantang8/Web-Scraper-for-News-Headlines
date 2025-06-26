# Web-Scraper-for-News-Headlines

# 📰 TOI News Headline Scraper

This Python script automatically scrapes top headlines from the [Times of India](https://timesofindia.indiatimes.com) homepage and saves them into a `.txt` file on your Desktop. It also opens the file automatically after execution.

## 🚀 Features

- Scrapes all visible news headlines
- Filters short/non-headline links
- Saves output to `toi_headlines.txt` on Desktop
- Automatically opens the file (Windows only)

---

## 🧰 Tools Used

- Python 3
- `requests` – for fetching HTML content
- `BeautifulSoup` (from `bs4`) – for parsing HTML
- `os` – to handle file paths and open the file

---

## 📦 Installation

1. Make sure you have Python 3 installed.
2. Install dependencies:

```bash
pip install requests beautifulsoup4
