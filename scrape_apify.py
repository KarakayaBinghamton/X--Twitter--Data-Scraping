# scrape_apify.py
# Description: Collects tweets using a pre-built scraper on the Apify platform.
# This method requires an Apify account and API token.

import os
import json
import pandas as pd
from apify_client import ApifyClient

# --- Configuration ---
# Load the Apify token securely from an environment variable
apify_token = os.getenv('APIFY_TOKEN')
if not apify_token:
    raise ValueError("APIFY_TOKEN environment variable not found. Please set it before running.")

# All non-sensitive settings are loaded from a separate JSON file.
# This makes the script easy to configure without changing the code.
try:
    with open('apify_config.json') as f:
        config = json.load(f)
    print("Configuration file 'apify_config.json' loaded successfully.")
except FileNotFoundError:
    print("Error: 'apify_config.json' not found. Please create it.")
    exit(1)
except json.JSONDecodeError:
    print("Error: 'apify_config.json' is not a valid JSON file.")
    exit(1)

# --- Main Scraping Logic ---
try:
    # Initialize the ApifyClient with your API token
    client = ApifyClient(apify_token)

    # Prepare the input for the Apify Actor, using settings from the config file
    run_input = {
        "searchTerms": config.get('searchTerms', []),
        "tweetLanguage": config.get('tweetLanguage', 'en'),
        "sort": config.get('sort', 'Top')
    }

    # ID of the Twitter Scraper Actor on the Apify platform
    actor_id = config.get('actorId', 'your_actor_id_here') # e.g., '61RPP7dywgiy0JPD0'

    print("Running the Apify scraper actor...")
    # Run the actor and wait for it to finish
    run = client.actor(actor_id).call(run_input=run_input)
    print("Scraper run initiated successfully.")

    print("Fetching results from the dataset...")
    # Fetch the results from the actor's default dataset
    results = client.dataset(run['defaultDatasetId']).list_items().items
    print(f"Results fetched. Found {len(results)} items.")

    # --- Save to CSV ---
    if results:
        df = pd.DataFrame(results)
        output_filename = 'tweets_apify.csv'
        df.to_csv(output_filename, index=False)
        print(f"Results saved to {output_filename}")
    else:
        print("No results were found to save.")

except Exception as e:
    print(f"An error occurred during the Apify process: {e}")
    exit(1)