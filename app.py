from flask import Flask
from scipy.spatial import distance as dist
from imutils.video import VideoStream
from imutils import face_utils
from threading import Thread
import sys
import numpy as np
import playsound
import argparse
import imutils
import time
import dlib
import cv2
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def sucesso():
    return 'sucesso'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
