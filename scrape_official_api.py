# scrape_official_api.py
# Description: Collects tweets using the official Twitter API v2 user timeline endpoint.
# Requires a developer account and a Bearer Token.

import os
import requests
import pandas as pd
import json
import time

# --- Configuration ---
# Load the Bearer Token securely from an environment variable
bearer_token = os.getenv('BEARER_TOKEN')
if not bearer_token:
    raise ValueError("BEARER_TOKEN environment variable not found. Please set it before running.")

# List of usernames to collect tweets from
usernames = ["BarisAtay", "TwitterDev"]

# --- API Functions ---
def create_headers(token):
    """Creates the authorization header required by the Twitter API."""
    return {"Authorization": f"Bearer {token}"}

def connect_to_endpoint(url, headers, params):
    """Sends a request to the specified API endpoint and returns the JSON response."""
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        raise Exception(f"Request returned an error: {response.status_code} {response.text}")
    return response.json()

def get_user_id(username, headers):
    """Fetches the user ID for a given username."""
    url = f"https://api.twitter.com/2/users/by/username/{username}"
    json_response = connect_to_endpoint(url, headers, {})
    if "data" in json_response:
        return json_response["data"]["id"]
    else:
        raise Exception(f"Could not find user ID for username: {username}")

# --- Main Logic ---
all_user_tweets = []

for username in usernames:
    print(f"\n#### Starting collection for user: {username} ####")
    try:
        headers = create_headers(bearer_token)
        user_id = get_user_id(username, headers)
        
        url = f"https://api.twitter.com/2/users/{user_id}/tweets"
        
        # Parameters for the API request. You can customize these.
        # See Twitter API documentation for all available fields.
        query_params = {
            'start_time': "2017-06-24T00:00:01Z",
            'end_time': "2018-06-23T23:59:59Z",
            'max_results': 100,
            'tweet.fields': 'created_at,public_metrics,lang'
        }
        
        pagination_token = None
        page_count = 0

        # Paginate through results until there are no more pages
        while True:
            page_count += 1
            print(f"Fetching page {page_count} for {username}...")
            
            # Set the pagination token for requests after the first one
            if pagination_token:
                query_params['pagination_token'] = pagination_token

            # Make the API call
            json_response = connect_to_endpoint(url, headers, query_params)
            result_count = json_response['meta'].get('result_count', 0)

            if result_count > 0:
                # Add username to each tweet object for context
                for tweet in json_response['data']:
                    tweet['username'] = username
                    all_user_tweets.append(tweet)
            
            # Check if there is a next page of results
            pagination_token = json_response['meta'].get('next_token', None)
            if not pagination_token:
                print(f"Finished collection for {username}. No more pages.")
                break # Exit the while loop for this user

            # Respect API rate limits before the next request
            print("Waiting to respect API rate limits...")
            time.sleep(5) # Adjust sleep time as needed for your API access level

    except Exception as e:
        print(f"An error occurred for user {username}: {e}")
        continue # Move to the next user

# --- Save to CSV ---
if all_user_tweets:
    df = pd.DataFrame(all_user_tweets)
    output_filename = "tweets_official_api_2018.csv"
    df.to_csv(output_filename, index=False)
    print(f"\nAll data saved to {output_filename}")
else:
    print("\nNo tweets were collected.")