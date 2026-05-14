from flask import Flask, request, redirect
from yt_dlp import YoutubeDL

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
        "format": "best"
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

        video_url = info["url"]

    return redirect(video_url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
