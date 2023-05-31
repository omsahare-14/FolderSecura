import cv2
import os
import warnings

warnings.filterwarnings("ignore")

def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    else:
        pass

def capture():
    videoCaptureObject = cv2.VideoCapture(0)            
    result = True
    while(result):
        ret, frame = videoCaptureObject.read()
        save_to = "C:/FolLockCaptured"
        create_folder(save_to)
        cv2.imwrite(save_to+"\\captured.jpg", frame)

        result = False
        videoCaptureObject.release()
        cv2.destroyAllWindows()
        run = False
        break