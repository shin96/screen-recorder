import datetime

from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics

screen_width = 1920  # GetSystemMetrics(0)
screen_height = 1080  # GetSystemMetrics(1)
FPS = 10.0
time = datetime.datetime.now().strftime('%Y_%m_%d-%H_%M')
file_name = str(time) + '.mp4'
web_cam = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
print(screen_width, screen_height)
captured_video = cv2.VideoWriter(file_name, fourcc, FPS, (screen_width, screen_height))

while True:
    img = ImageGrab.grab(bbox=(0, 0, screen_width, screen_height))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    _, frame = web_cam.read()
    frame_height, frame_width, _ = frame.shape
    img_final[0:frame_height, 0: frame_width, :] = frame[0:frame_height, 0: frame_width, :]
    cv2.imshow('screen_rec', img_np)
    captured_video.write(img_final)
    if cv2.waitKey(10) == ord('q'):
        break
