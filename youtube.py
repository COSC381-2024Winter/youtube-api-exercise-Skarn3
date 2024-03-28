# youtube.py
import sys
import config
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Set up API key and service parameters
DEVELOPER_KEY = config.YOUTUBE_API_KEY
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(query_term, max_results):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified query term.
    search_response = youtube.search().list(
        q=query_term,
        part="snippet",
        type="video",
        maxResults=max_results
    ).execute()

    return search_response

if __name__ == "__main__":
    # Prompt the user for necessary input
    query_term = input("Enter the search query: ")
    max_results = int(input("Enter the maximum number of results: "))

    # Perform the YouTube search
    search_response = youtube_search(query_term, max_results)

    # Print the search response
    print(search_response)
