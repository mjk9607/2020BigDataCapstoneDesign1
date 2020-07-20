from flask import Flask, render_template, Response
from camera import VideoCamera

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

def generator(camera):
  # while True:
    yield (b'--frame\r\n'b'Contents-Type: image/jpeg\r\n\r\n' + camera.get_frame() + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
  return Response(generator(VideoCamera()), mimetype = 'multipart/x-mixed-replace; boundary=frame')

@app.route('/capture')
def capture():
  return VideoCamera().get_frame()


if __name__ == '__main__':
  
  aHost = 'localhost'
  aPort = '5000'
  aDebug = True

  try:
    app.run(host = aHost, port = aPort, debug = aDebug)
  except:
    print('Unable to open Port : ' + aPort)
