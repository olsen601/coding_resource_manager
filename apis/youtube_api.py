from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os
from key import key





def video(category):

    DEVELOPER_KEY = key
    YOUTUBE_API_SERVICE_NAME = 'youtube'
    YOUTUBE_API_VERSION = 'v3'

    try:
        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
        developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
        search_response = youtube.search().list(
            q= category,
            part="id,snippet",
            maxResults=2,
            type='videos',
            safeSearch='strict'
        ).execute()

        result = search_response.get('items', [])[0]
        print(result)

        title = result['snippet']['title']
        video_id = result['id']['videoId']

        return{ 'title': title, 'video_id': video_id }

    except Exception as e:
        print(e)

      # videos = []
      # channels = []
      # playlists = []

      # Add each result to the appropriate list, and then display the lists of
      # matching videos, channels, and playlists.
      # for search_result in search_response.get("items", []):
      #   if search_result["id"]["kind"] == "youtube#video":
      #     videos.append("%s (%s)" % (search_result["snippet"]["title"],
      #                                search_result["id"]["videoId"]))
      #   elif search_result["id"]["kind"] == "youtube#channel":
      #     channels.append("%s (%s)" % (search_result["snippet"]["title"],
      #                                  search_result["id"]["channelId"]))
      #   elif search_result["id"]["kind"] == "youtube#playlist":
      #     playlists.append("%s (%s)" % (search_result["snippet"]["title"],
      #                                   search_result["id"]["playlistId"]))

        # return render_template(videos('/.html', videos = videos))

      # return ("Videos:\n", "\n".join(videos), "\n")
      #       ("Channels:\n", "\n".join(channels), "\n"),
      #       ("Playlists:\n", "\n".join(playlists), "\n")


if __name__ == "__main__":
    print(video('video'))
# argparser.add_argument("--q", help="Search term", default="Python Code")
# argparser.add_argument("--max-results", help="Max results", default=15)
# args = argparser.parse_args()
