import cv2 as cv 
import numpy as np

cam = cv.VideoCapture(0)

Trit = np.array([
    [0.299, 0.587, 0.114],
    [0.299,  0.587, 0.114],
    [0.299,  0.587, 0.114]
])

while True:
    ret, frame = cam.read()
    
    # If frame read successfully
    if not ret:
        break
    b,g,r = cv.split(frame)
    
    b = np.clip(b + 80,0,255).astype(np.uint8)


    ff = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    f = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    fff = cv.cvtColor(frame,cv.COLOR_BGR2YUV)
    cv.imshow('ff',f)
    cv.imshow('fff',ff)
    cv.imshow('ffff',fff)
    # Show the frame
    cv.imshow('Original',frame)

    # Press 'q' to quit
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam and close windows
cam.release()
cv.destroyAllWindows()
