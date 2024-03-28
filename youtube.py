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

    # Call the search.list method to retrieve videos matching the specified query term.
    search_response = youtube.search().list(
        q=query_term,
        part="snippet",
        type="video",
        maxResults=max_results
    ).execute()

    # Extract the videos from the search response
    videos = search_response.get("items", [])

    return videos

if __name__ == "__main__":
    # Prompt the user for the search query and max results
    query_term = input("Enter the search query: ")
    max_results = int(input("Enter the maximum number of results: "))

    # Perform the YouTube search
    video_list = youtube_search(query_term, max_results)

    # Print the list of videos
    print(video_list)
