import numpy as np
import cv2
import time
import os
from PIL import Image

face_recognizer = cv2.face.LBPHFaceRecognizer_create();
path = 'Dataset'

def getImagesWithId(path):
    img_paths = [os.path.join(path, f) for f in os.listdir(path)]
    for path in img_paths:
        print(path)

getImagesWithId(path)

