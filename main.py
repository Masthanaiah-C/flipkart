
import cv2
import motion_detection as m

IP_WEB_CAM_URL = 'https://192.168.185.239:8080/video'
cap = cv2.VideoCapture(IP_WEB_CAM_URL)
POINTS = m.initialise(cap)
# THESE ARE THE COORDINATES OF THE ARENA WE WRAP PERSPECT THIS TO DETECT MOTION ONLY IN THE ARENA
# OR YOU CAN ENTER THESE VALUES MANUALLY BEFORE EXECUTION

m.motionDetection(cap, POINTS)
