from flask import Flask, render_template, Response
from cameratest import VideoCamera
import time
import threading

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

def generator(camera):
  while True:
    yield (b'--frame\r\n'b'Contents-Type: image/jpeg\r\n\r\n' + camera.get_frame() + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
  return Response(generator(VideoCamera()), mimetype = 'multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = '5000', debug = True)
