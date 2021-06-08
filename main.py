from flask import Flask, request, send_file
from pytube import YouTube
import logging
import sys

"""
Flask YouTube Video Downloader - Python Marketer
https://pythonmarketer.com/2020/10/07/making-a-youtube-video-downloader-with-pythons-flask-and-pytube3-libraries/
"""
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
app = Flask(__name__)

@app.route("/")
def youtube_downloader():
    """Render HTML form to accept YouTube URL."""
    html_page = f"""<html><head>
                    <Title>YouTube Downloader</Title></head>
                    <body><h2>Enter URL to download YouTube Vids!</h2>
                    <div class="form">
                    <form action="/download_video" method="post">
                    <input type="text" name="URL">
                    <input type="submit" value="Submit">
                    </form></div><br><br>
                    </body></html>"""
    return html_page

@app.route("/download_video", methods=["GET","POST"])
def download_video():
    """
    First pytube downloads the file locally in pythonanywhere:
    /home/your_username/video_name.mp4

    Then use Flask's send_file() to download the video
    to the user's Downloads folder.
    """
    try:
        youtube_url = request.form["URL"]
        local_download_path = YouTube(youtube_url).streams[0].download()
        fname = local_download_path.split("//")[-1]
        return send_file(fname, as_attachment=True)
    except:
        logging.exception("Failed download")
        return "Video download failed!"
if __name__ == '__main__':
    app.run(debug=False ,host = '0.0.0.0')
