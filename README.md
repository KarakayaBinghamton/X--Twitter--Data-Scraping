# 🐦 Twitter (X) Data Scraping Toolkit

## 📖 Overview
This repository contains a collection of Python scripts designed to collect tweets using **three distinct methods**. It serves as a toolkit for researchers, developers, and data analysts, showcasing different approaches to data acquisition from **X (formerly Twitter)**, each with unique advantages and use cases.  

⚠️ **Disclaimer:** This project is intended for **educational and research purposes only**. Users must comply with the [X/Twitter Developer Agreement](https://developer.twitter.com/en/developer-terms/agreement-and-policy), [Apify Terms of Service](https://apify.com/terms-of-service), and all applicable laws. Respect user privacy and do not misuse collected data.

---

## ✨ Features
- Three independent scraping methods:
  - **Legacy `snscrape`** — No API keys required, great for historical analysis.
  - **Apify Platform** — Cloud-based scraper with scalable infrastructure.
  - **Official Twitter API v2** — Policy-compliant, reliable, supports advanced queries.  
- Saves results as **CSV files** for easy analysis.  
- Flexible configuration and simple setup.  

---

## ⚙️ Collection Methods

### 1. Legacy `snscrape` (`scrape_legacy.py`)
- Uses the `snscrape` library (no official API keys needed).  
- Ideal for historical tweet analysis or when you don’t have API access.  
- ⚠️ Note: This method may break if Twitter changes its structure.  

### 2. Apify Cloud Scraper (`scrape_apify.py`)
- Leverages the [Apify](https://apify.com/) platform for scraping at scale.  
- Requires an **Apify account** and **API token**.  
- Offloads infrastructure to a third-party service (robust for large jobs).  

### 3. Official Twitter API v2 (`scrape_official_api.py`)
- Uses the official [Twitter API v2](https://developer.twitter.com/en/docs/twitter-api).  
- Requires a **Twitter Developer account** and a **Bearer Token**.  
- Demonstrates handling **pagination, rate limits, and credential management**.  
- Most reliable and policy-compliant method.  

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/KarakayaBinghamton/X--Twitter--Data-Scraping.git
cd X--Twitter--Data-Scraping


2. Install Dependencies

pip install -r requirements.txt


3. Set Environment Variables

You will need to set credentials for Apify and the Official API methods.

macOS / Linux (bash):

export APIFY_TOKEN="your_apify_token_here"
export BEARER_TOKEN="your_twitter_bearer_token_here"

Windows (Command Prompt):

set APIFY_TOKEN="your_apify_token_here"
set BEARER_TOKEN="your_twitter_bearer_token_here"

🛠 Usage

Run one of the scraping methods:

Legacy snscrape:

python scrape_legacy.py


Apify scraper:

python scrape_apify.py


Official Twitter API v2:

python scrape_official_api.py


👉 Each script will generate a .csv file with the collected tweets in the project directory.


.
├── scrape_legacy.py          # Method 1: snscrape
├── scrape_apify.py           # Method 2: Apify Platform
├── scrape_official_api.py    # Method 3: Official API v2
├── apify_config.json         # Apify configuration file
├── requirements.txt          # Python dependencies
├── .gitignore                # Ignored files
└── README.md                 # Project documentation


📜 License

This project is licensed under the MIT License.


