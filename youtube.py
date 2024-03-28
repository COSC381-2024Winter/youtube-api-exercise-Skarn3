# youtube.py
import sys
import config
import json
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Set up API key and service parameters
DEVELOPER_KEY = config.YOUTUBE_API_KEY
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(query_term, max_results):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    all_videos = []

    # Perform search for each page
    next_page_token = None
    for _ in range(5):  # Fetch from 5 pages
        # Call the search.list method to retrieve videos matching the specified query term.
        search_response = youtube.search().list(
            q=query_term,
            part="snippet",
            type="video",
            maxResults=max_results,
            pageToken=next_page_token  # Include page token for pagination
        ).execute()

        # Extract the videos from the search response
        videos = search_response.get("items", [])
        all_videos.extend(videos)

        # Get the next page token for the next iteration
        next_page_token = search_response.get("nextPageToken")
        if not next_page_token:
            break  # Break the loop if there are no more pages

    return all_videos

if __name__ == "__main__":
    # Prompt the user for input
    query_term = input("Enter the search query: ")
    max_results = int(input("Enter the maximum number of results per page: "))

    # Perform the YouTube search for multiple pages
    all_videos = youtube_search(query_term, max_results)

    # Return the JSON data
    print(json.dumps(all_videos, indent=2))
