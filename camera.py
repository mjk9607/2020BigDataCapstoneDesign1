import cv2

class VideoCamera(object):
  def __init__(self):
    self.video = cv2.VideoCapture(0)

  def __del__(self):
    self.video.release()

  def get_frame(self):
    ret, frame = self.video.read()

    ret, jpeg = cv2.imencode('.jpeg', frame)
    return jpeg.tobytes()

  def get_size(self):
    width = self.video.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = self.video.get(cv2.CAP_PROP_FRAME_HEIGHT)

    return width, height