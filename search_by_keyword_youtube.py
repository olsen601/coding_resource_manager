from flask import Flask, request, render_template
from apis import youtube_api
from key import key



app = Flask(__name__)

@app.route('/')
def home_page():

    return render_template("index.html")

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = key
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

@app.route('/get-video')
def get_video():


    search_query = request.args.get("python code")

    video = youtube_api.video(search_query)

    if video:
        return render_template('video.html', video=video)
    else:
        return render_template('error.html')

if __name__=='__main__':
    app.run()
