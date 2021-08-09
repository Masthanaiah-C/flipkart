import cv2 
import numpy as np
def destroy():
    cv2.destroyAllWindows()
    
def edge_board(frame):
    
        edge_G = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(edge_G,100,150,apertureSize=3)
        cv2.imshow('edges',edges)

        # detect lines in the image using hough lines technique
        lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=50,maxLineGap=3)
        
        # iterate over the output lines and draw them
        try:
            for line in lines:
                    x1, y1, x2, y2 = line[0]
                    cv2.line(frame, (x1, y1), (x2, y2), (20, 220, 20), 2)
        except:
            pass
        cv2.imshow('frame',frame)

        
def capture(url):
    cap = cv2.VideoCapture(url)
    while(True):
        ret, frame = cap.read()
        if frame is not None:
            cv2.imshow('stream',frame)        
        edge_board(frame);
        q = cv2.waitKey(1)
        if q == ord("q"):
            break
    
