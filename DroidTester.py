import cv2
import numpy as np
import matplotlib.pyplot as plt


##img1 = cv2.imread('Black-hammer.png')
##img2 = cv2.imread('InkedBlack2_LI.jpg')
##
##add = img1 + img2
##
##cv2.imshow('add', add)
##cv2.waitKey(0)
##cv2.destroyAllWindows()




##
##
##img = cv2.imread('test.png', cv2.IMREAD_COLOR)
##img[55,55] = [0,0,0]
##px = img[55,55]
##
##img[100:150, 100:150] = [0,0, 0]
##
##cv2.imshow('image', img)
##cv2.waitKey(0)
##cv2.destroyAllWindows()
##
##
##img = cv2.imread('test.png', cv2.IMREAD_COLOR)
##cv2.line(img, (0,0), (150,150), (255, 255, 255), 5)
##cv2.rectangle(img, (15, 25), (200, 150), (250, 250, 250), 2)
##cv2.circle(img, (500, 500), 30, (0,0,255), -1)
##font = cv2.FONT_HERSHEY_SIMPLEX
##cv2.putText(img, 'FIRE YOUR LAzERS!!!', (0,500), font, 1, (200,255,255), 2, cv2.LINE_AA)
##cv2.imshow('image', img)
##cv2.waitKey(0)
####cv2.destroyAllWindows()

cap =  cv2.VideoCapture(0)

##fourcc = cv2.VideoWriter_fourcc(*'XVID')
##out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()
##
##img = cv2.imread('test.png', cv2.IMREAD_GRAYSCALE)
#GRAYSCALE = 0
#IMREAD_COLOR = 1
#IMREAD_UNCHANGED = -1
##cv2.imshow('image', img);
##cv2.waitKey(0)
##cv2.destroyAllWindows()
##plt.imshow(img, cmap='gray', interpolation='bicubic')
##plt.show()
