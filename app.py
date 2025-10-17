from screenshot_vid import ScreenshotVideo
from download import GetAndDownloadVideo

url = "https://www.tiktok.com/t/ZP8Aqm2X8/"
name = "officialTest.mp4"

download = GetAndDownloadVideo()
screenshot = ScreenshotVideo()

video = download.download_url(url, name)

screenshot.capture_frames(video, 3)


