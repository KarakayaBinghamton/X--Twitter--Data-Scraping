# scrape_legacy.py
# Description: Scrapes tweets using the snscrape library, a method that worked before the 2023 Twitter API changes.
# This script does not require API keys.

import snscrape.modules.twitter as sntwitter
import pandas as pd

# --- Configuration ---
# It's best practice to load a long list of usernames from a file.
# For this example, we'll use a short list.
# To use your full list, you could do:
# with open('usernames.txt', 'r') as f:
#     usernames_to_scrape = [line.strip() for line in f]
usernames_to_scrape = [
    'Twitter Handle 1',
    'Twitter Handle 2',
    'Twitter Handle 3'
]

# Set the time frame for the search
since_date = '2017-06-24'
until_date = '2018-06-24'

# Set a limit on the total number of tweets to collect
max_tweets_total = 5000

# --- Main Scraping Logic ---
tweets_list = []
print("Starting tweet collection...")

# The scraper iterates through each username provided
for username in usernames_to_scrape:
    if len(tweets_list) >= max_tweets_total:
        print(f"Reached the total limit of {max_tweets_total} tweets. Stopping.")
        break # Exit the main loop if the total limit is reached

    print(f"Scraping for user: {username}...")
    try:
        # Create a search query for a specific user within a date range and language
        query = f"from:{username} since:{since_date} until:{until_date} lang:tr"
        
        # Use sntwitter to get the items from the search
        for tweet in sntwitter.TwitterSearchScraper(query).get_items():
            # Check if we have reached the total limit inside the loop
            if len(tweets_list) >= max_tweets_total:
                break
            
            # Append the desired tweet information to our list
            tweets_list.append([
                tweet.date,
                tweet.id,
                tweet.user.username,
                tweet.content,
                tweet.user.location,
                tweet.url
            ])

    except Exception as e:
        print(f"An error occurred while scraping for {username}: {e}")
        continue # Move to the next user if an error occurs

print(f"Collection complete. Total tweets gathered: {len(tweets_list)}")

# --- Save to CSV ---
# Convert the list of tweets into a pandas DataFrame
df = pd.DataFrame(
    tweets_list,
    columns=['Date', 'ID', 'Username', 'Content', 'Location', 'URL']
)

# Save the DataFrame to a CSV file
output_filename = 'tweets_legacy_2018.csv'
df.to_csv(output_filename, index=False)
print(f"Data saved to {output_filename}")