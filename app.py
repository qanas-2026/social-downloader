from flask import Flask, request, send_file
from yt_dlp import YoutubeDL
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Server Running"

@app.route("/download")
def download():

    url = request.args.get("url")

    if not url:
        return "No URL"

    ydl_opts = {
        'format': 'best',
        'outtmpl': 'video.%(ext)s'
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    for file in os.listdir():

        if file.startswith("video"):

            return send_file(
                file,
                as_attachment=True
            )

    return "Error"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
