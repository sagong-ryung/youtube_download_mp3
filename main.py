from yt_dlp import YoutubeDL


class YoutubeDowonloader:
    def __init__(self) -> None:
        """Initialize the YoutubeDowonloader

        Args:
            url_list (list): list of urls
        """

        self.output_path = "/result"
        self.ydl_opts = {
            "format": "mp3/bestaudio/best",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                }
            ],
            "outtmpl": f"{self.output_path}/%(title)s.%(ext)s",
        }
    
    def download(self, url_list: list):
        """Download the given urls

        Args:
            urls (list): list of urls
        """
        with YoutubeDL(self.ydl_opts) as ydl:
            result = ydl.download(url_list)


def main():
    URL_LIST = [
        "https://www.youtube.com/XXXXXXXXXX",
        ]

    yd = YoutubeDowonloader(URL_LIST)
    yd.download(URL_LIST)

main()

