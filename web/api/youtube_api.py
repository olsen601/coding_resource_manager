from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os
from key import key
import logging

def video(search_query):

    DEVELOPER_KEY = key
    YOUTUBE_API_SERVICE_NAME = 'youtube'
    YOUTUBE_API_VERSION = 'v3'

    try:
        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
        developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
        search_response = youtube.search().list(
            q= search_query,
            part="id,snippet",
            maxResults=2,
            type='videos',
            safeSearch='strict'
        ).execute()
        logging.info('youtube API call started')

        result = search_response.get('items', [])[0]

        title = result['snippet']['title']
        video_id = result['id']['videoId']
        # print('title: ', title, "video: ", video )
        return{ 'title': title, 'video_id': video_id }

    except Exception as e:
        print(e)
        logging.info('youtube exception caught')


if __name__ == "__main__":
    print(video('video'))
# argparser.add_argument("--q", help="Search term", default="Python Code")
# argparser.add_argument("--max-results", help="Max results", default=15)
# args = argparser.parse_args()
