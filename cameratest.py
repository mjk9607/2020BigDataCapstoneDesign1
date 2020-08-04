import cv2
import numpy as np
import pyautogui

class VideoCamera(object):
  def get_frame(self):
    frame = pyautogui.screenshot(region = (400, 400, 400, 400))
    img_frame = np.array(frame)
    img_frame = cv2.cvtColor(img_frame, cv2.COLOR_RGB2BGR)

    ret, jpeg = cv2.imencode('.jpeg', img_frame)
    return jpeg.tobytes()
