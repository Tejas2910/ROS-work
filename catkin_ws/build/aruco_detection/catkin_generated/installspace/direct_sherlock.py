#!/usr/bin/env python2

import numpy as np
import cv2
import cv2.aruco as aruco
import sys
import math
import time


def detect_ArUco(img):
	## function to detect ArUco markers in the image using ArUco library
	## argument: img is the test image
	## return: dictionary named Detected_ArUco_markers of the format {ArUco_id_no : corners}, where ArUco_id_no indicates ArUco id and corners indicates the four corner position of the aruco(numpy array)
	## 		   for instance, if there is an ArUco(0) in some orientation then, ArUco_list can be like
	## 				{0: array([[315, 163],
	#							[319, 263],
	#							[219, 267],
	#							[215,167]], dtype=float32)}
    Detected_ArUco_markers = {}
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_250)
    parameters = aruco.DetectorParameters_create()
    corners, ids, _ = aruco.detectMarkers(gray, aruco_dict, parameters = parameters) 
    i = 0
    
    try:
        for id in ids:
            for id_Number in id:
                Detected_ArUco_markers[id_Number] = corners[i][0]    

    except TypeError:
        print("No aruco in front of me")

    i += 1
    return Detected_ArUco_markers


def mark_ArUco(img,Detected_ArUco_markers):
	## function to mark ArUco in the test image as per the instructions given in problem statement
	## arguments: img is the test image 
	##			  Detected_ArUco_markers is the dictionary returned by function detect_ArUco(img)
	## return: image helping sherlock to solve maze 

    ids = Detected_ArUco_markers.keys()
    print(Detected_ArUco_markers)
    centre_aruco = {}
    top_centre = {}

    try:
        for id in ids:
            corners = Detected_ArUco_markers[id]
            for i in range(0, 4):
                cv2.circle(img,(int(corners[i][0]), int(corners[i][1])), 5, (0,0,255), -1)
            centre_aruco[id] = (corners[0]+corners[1]+corners[2]+corners[3])/4
            top_centre[id] = (corners[0]+corners[1])/2
            cv2.line(img, (int(centre_aruco[id][0]), int(centre_aruco[id][1])), (int(top_centre[id][0]), int(top_centre[id][1])), (255, 0, 0), 5)

    except TypeError:
        print("No aruco in front of me")

    return img
