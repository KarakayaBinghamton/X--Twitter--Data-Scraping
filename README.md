# Twitter Data Toolkit 🐦

## 📝 Overview

This project is a collection of Python scripts designed to collect tweet data using three distinct methods. It serves as a toolkit for researchers, developers, and data analysts, showcasing different approaches to data acquisition from X (formerly Twitter), each with its own advantages and use cases.

---

## ✨ Features

This toolkit includes three different collection methods:

1.  **Legacy `snscrape` Method (`scrape_legacy.py`):**
    * Uses the `snscrape` library to scrape tweets without requiring official API keys.
    * Represents a powerful technique that was widely used before the 2023 API policy changes.
    * Ideal for historical analysis or projects that don't have access to the official API.

2.  **Third-Party Apify Platform (`scrape_apify.py`):**
    * Leverages the Apify platform to run a pre-built cloud scraper.
    * A robust, scalable solution that offloads the scraping infrastructure to a third-party service.
    * Requires an Apify account and API token.

3.  **Official X/Twitter API v2 (`scrape_official_api.py`):**
    * Uses the official Twitter API v2, the most reliable and policy-compliant method for data collection.
    * Requires a Twitter Developer account and a Bearer Token.
    * Demonstrates handling pagination, rate limits, and secure credential management.

---

## ⚠️ Ethical Disclaimer

This toolkit is intended for educational and research purposes only. Users are responsible for complying with the X (Twitter) Developer Agreement and Policy, the Apify Terms of Service, and all applicable laws. Respect user privacy and do not misuse the collected data.

---

## 🚀 Getting Started

Follow these steps to set up and run the project.

### 1. Clone the Repository
```sh
git clone [https://github.com/KarakayaBinghamton/X--Twitter--Data-Scraping.git](https://github.com/KarakayaBinghamton/X--Twitter--Data-Scraping.git)
cd X--Twitter--Data-Scraping


2. Set Up Environment Variables
This project requires API keys for the Apify and Official API methods. Store them securely as environment variables.

On macOS or Linux:

Bash

export APIFY_TOKEN="your_apify_token_here"
export BEARER_TOKEN="your_twitter_bearer_token_here"
On Windows (Command Prompt):

Bash

set APIFY_TOKEN="your_apify_token_here"
set BEARER_TOKEN="your_twitter_bearer_token_here"
3. Install Dependencies
Install all the required Python libraries using the requirements.txt file.

Bash

pip install -r requirements.txt
🛠️ Usage
Before running a script, ensure you have configured it correctly (e.g., set usernames in scrape_legacy.py or search terms in apify_config.json).

To run the legacy snscrape method:

Bash

python scrape_legacy.py
To run the Apify cloud scraper:

Bash

python scrape_apify.py
To run the official Twitter API v2 collector:

Bash

python scrape_official_api.py
Each script will save its output as a .csv file in the project directory.

📂 Project Structure
.
├── scrape_legacy.py          # Method 1: snscrape
├── scrape_apify.py           # Method 2: Apify Platform
├── scrape_official_api.py    # Method 3: Official API v2
├── apify_config.json         # Configuration for the Apify script
├── requirements.txt          # Python library dependencies
├── .gitignore                # Files to be ignored by Git
└── README.md                 # This file


📜 License
This project is licensed under the MIT License.
