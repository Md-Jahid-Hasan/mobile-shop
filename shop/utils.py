import cv2 as cv
import threading


class VideoCamera(object):

    def __init__(self):
        self.video = cv.VideoCapture(0)
        self.grabbed, self.frame = self.video.read()
        print(self.frame)
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()