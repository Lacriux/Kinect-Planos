#!/usr/bin/env python

import freenect
import cv
import cv2
import numpy as np

import time
import sys

threshold = 100
current_depth = 480

def change_threshold(value):
    global threshold
    threshold = value

def change_depth(value):
    global current_depth
    current_depth = value

def show_depth():
	global threshold
	global current_depth

	depth, timestamp = freenect.sync_get_depth()	
	depth = 255 * np.logical_and(depth >= current_depth - threshold, depth <= current_depth + threshold)
	depth = depth.astype(np.uint8)
	
	return depth
	
def show_video(image, image_name):	
	cv2.namedWindow(image_name)
	cv2.createTrackbar(image_name + ' threshold', image_name, threshold, 600, change_threshold)
	cv2.createTrackbar(image_name + ' depth', image_name, current_depth, 600, change_depth)
	
	
def show_image(imagen, mensaje):
	
	cv2.imshow(mensaje, imagen)

def flip_image(imagen):
	#mirror image
	#http://docs.opencv.org/modules/core/doc/operations_on_arrays.html#void flip(InputArray src, OutputArray dst, int flipCode)
	
	imagen = cv2.flip(imagen,1)
	
	return imagen

if __name__ == "__main__":
	print "Presione 'q' para salir"
	
			
	while 1:
		image = show_depth()
		image = flip_image(image)
		image2 =  cv2.imread ('/home/electrizarte/Kinect-Planos/Image_reading/silueta.jpeg', 0)
		
		#image = rslt_fc['img']
		
						
		show_image(image, "matching")
		show_video(image, "matching")
		show_image(image2, "prueba")
		show_video(image2, "prueba")
		
		c = cv2.waitKey(10)
		
		if 'q' == chr(c & 255):
			cv2.destroyAllWindows()			
			break
			output.close()
