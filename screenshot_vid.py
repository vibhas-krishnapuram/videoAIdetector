import cv2

class ScreenshotVideo:
    def __init__(self) -> None:
        pass

    def capture_frames(self, video_path, interval=3):
        cap = cv2.VideoCapture(video_path)
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        frame_count = 0
        saved = 0

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            
            if frame_count % (fps * interval) == 0:
                filename = f"screenshots/frame_{saved}.jpg"
                cv2.imwrite(filename, frame)
                print(f"Saved {filename}")
                saved += 1

            frame_count += 1

        cap.release()



#video = "downloads/tiktok.mp4"

#capture = ScreenshotVideo()

#capture.capture_frames(video)


