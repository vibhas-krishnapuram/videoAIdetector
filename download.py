import requests
import os

class GetAndDownloadVideo:
    def __init__(self):
        self.path = "./downloads"
        os.makedirs(self.path, exist_ok=True)

    def get_video_url(self, url):
        headers = {'url': url}
        response = requests.get(url, headers=headers) 

        spl = response.url.split('/') 
        if spl[4] == 'video': 
            video_id = spl[5].split('?')[0] 
            request_url = f'https://www.tikwm.com/video/media/play/{video_id}.mp4' 
            response = requests.get(request_url, headers=headers) 
            video_link = response.url 
        if video_link:
            return video_link 
        else: 
            return False


    def download_url(self, orig_link, file_name="DownloadFile.mp4"):

        link = self.get_video_url(orig_link)

        if not link:
            return None

        save_path = os.path.join(self.path, file_name)

        try:
            video_response = requests.get(link, stream=True)
            video_response.raise_for_status()

            with open(save_path, 'wb') as f:
                f.write(video_response.content)
            
            return save_path
        except Exception as e:
            print(e)
            return None



test = "https://www.tiktok.com/t/ZP8AVbaFu/"
downloader = GetAndDownloadVideo()

downloader.download_url(test, "tiktok.mp4")