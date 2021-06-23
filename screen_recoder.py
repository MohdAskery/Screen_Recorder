# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 22:18:19 2021

@author: Mohd Askery Malik
"""

import cv2
import pyautogui as p 
import numpy as np

screen_size=p.size()

filePath=input("Enter File Path And Name: \n")

fps=20.0

fourcc=cv2.VideoWriter_fourcc(*"XVID")
# ================fileName,fouccc,fps,resolution
output=cv2.VideoWriter(filePath,fourcc,fps,screen_size);


# creat recordsing module
cv2.namedWindow("Live Recording..",cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live",(600,400))

while True:
    img=p.screenshot()
    frame=np.array(img)
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    cv2.resize(frame,(300,400))
    
    # cv2.imshow("screen", frame)
    output.write(frame)
    if cv2.waitKey(1) == ord("q"):
        break
    

cv2.destroyAllWindows()
output.release()  