import cv2
import numpy as np
import pyautogui
import threading

class cCamera(threading.Thread):
  def __init__(self):
    self.pic = pyautogui.screenshot(region = (0, 0, 700, 500))
    threading.Thread.__init__(self)

  def read(self):
    return self.pic

  def run(self):
    while True:
      self.pic = pyautogui.screenshot(region = (0, 0, 700, 500))


class VideoCamera(object):
  def __init__(self):
    self.video = cCamera()
    self.video.daemon = True
    self.video.start()

  def __del__(self):
    self.video.release()

  def get_frame(self):
    frame = self.video.read()
    img_frame = np.array(frame)
    img_frame = cv2.cvtColor(img_frame, cv2.COLOR_RGB2BGR)

    ret, jpeg = cv2.imencode('.jpg', img_frame)
    return jpeg.tobytes()