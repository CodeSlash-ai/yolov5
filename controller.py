"""
This script calls the YOLOv5 model and returns the results in the form of an image. 
"""

import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2


def handleImage(model, file_name):

    # running the model on the image
    results = model(file_name)

    # printing the results returned by the model
    results.print()

    results.show()

    # displaying the results in image format
    # while True:
    #     RGB_img = cv2.cvtColor(np.squeeze(results.render()), cv2.COLOR_BGR2RGB)
    #     cv2.imshow("YOLO", RGB_img)

    #     if cv2.waitKey(10) & 0xFF == ord('q'):
    #         break

    # cv2.destroyAllWindows()
    

    return

def handleVideo(model, file_name):
    cap = cv2.VideoCapture(file_name)
    while cap.isOpened():
        ret, frame = cap.read()
        
        #Make detections
        results = model(frame)

        cv2.imshow('YOLO', np.squeeze(results.render()))
        
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows() 

    return



def main():

    # loading the yolov5s model
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
    
    # storing the name of the file on which detection would run
    # file_name = input("Filename to run detection: ")
    file_name = "yolov5/data/images/bus.jpg"

    results = model(file_name)

    results.show()

    # extracting the last three characters to find out wether its an image or a video
    # last_three_chars = file_name[-3:]

    # if last_three_chars == "mp4":
        
    #     # process for video
    #     handleVideo(model, file_name)
    # elif last_three_chars == "jpg":

    #     # process for image
    #     handleImage(model, file_name)
    # else:
    #     print("ERROR! Filename is not correct. Only .jpg and .mp4 are supported.")
    #     return


if __name__ == "__main__":
    main()