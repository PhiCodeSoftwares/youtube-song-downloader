from pytube import YouTube
import ffmpeg
import time

class YoutubeSongDownloader:

    def __init__(self) -> None:
        self.counter = 0

    def dowload(self, url):
        yt = YouTube(url)

        print("Video Title:", yt.title)
        print("Video Length:", yt.length, "seconds")

        streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()

        output_filename = f'{self.counter}.mp4'

        start_time = time.time()

        stream = streams[-1]
        stream.download(filename=output_filename)

        self.extract_audio_from_video(output_filename)

        end_time = time.time()
        print(end_time - start_time)

    def extract_audio_from_video(self, input_video):
        output_audio = input_video.replace(".mp4", ".mp3")
        (
            ffmpeg
                .input(input_video)
                .output(output_audio)
                .run()
        )
    
downloader = YoutubeSongDownloader()
downloader.dowload('https://youtu.be/dX0CgkYJgbQ?si=6D_PQfotOF4yF1FP')
