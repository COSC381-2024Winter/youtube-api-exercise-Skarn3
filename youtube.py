# youtube.py
import sys
import config
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Set up API key and service parameters
DEVELOPER_KEY = config.YOUTUBE_API_KEY
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(query_term, max_results, page_token=None):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve videos matching the specified query term.
    search_response = youtube.search().list(
        q=query_term,
        part="snippet",
        type="video",
        maxResults=max_results,
        pageToken=page_token  # Include page token for pagination
    ).execute()

    # Extract the videos from the search response
    videos = search_response.get("items", [])
    next_page_token = search_response.get("nextPageToken")

    return videos, next_page_token

if __name__ == "__main__":
    # Prompt the user for the search query and max results
    query_term = input("Enter the search query: ")
    max_results = int(input("Enter the maximum number of results: "))

    # Perform the YouTube search for the first page
    first_page_videos, next_page_token = youtube_search(query_term, max_results)

    # Print the list of videos for the first page
    print("First Page Results:")
    for video in first_page_videos:
        print(video)

    # If there's a next page token, fetch the second page results
    if next_page_token:
        # Perform the YouTube search for the second page
        second_page_videos, _ = youtube_search(query_term, max_results, next_page_token)

        # Print the list of videos for the second page
        print("\nSecond Page Results:")
        for video in second_page_videos:
            print(video)
