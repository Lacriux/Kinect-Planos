
#!/usr/bin/env python

import freenect
import cv
import cv2
import numpy as np

import time
import sys

threshold = 100
current_depth = 480

fixed_threshold = 600
fixed_depth2 = 200
fixed_depth = 300

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
	
def show_depth2():
        global fixed_threshold
        global fixed_depth

        depth, timestamp = freenect.sync_get_depth()
       	depth = 255 * np.logical_and(depth >= fixed_depth- fixed_threshold, depth <= fixed_depth + fixed_threshold)
        depth = depth.astype(np.uint8)

        return depth

def show_depth3():
        global fixed_threshold
        global fixed_depth2

        depth, timestamp = freenect.sync_get_depth()
        depth = 255 * np.logical_and(depth >= fixed_depth2- fixed_threshold, depth <= fixed_depth2 + fixed_threshold)
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
		image2 = show_depth2()
		image2 = flip_image(image2)
		image4 = cv2.imread('paisaje.jpg', 1)
		#image4 = cv2.resize(image4, (640, 480))
		image6 = show_depth3()
		image6 = flip_image(image6)

		image4 = cv2.resize(image4, (1920, 1080))	

		image3 = image2 - image6 - image
		image3 = cv2.resize(image3, (1920, 1080))
		#image3 = cv2.subtract(image6,image2)
		#image3 = cv2.subtract(image, image3)
		image3 = cv2.cvtColor(image3, cv2.COLOR_GRAY2BGR)    
				
		#rows,cols,channels = image4.shape
		#roi = image4[0:rows, 0:cols]

		image5 = cv2.subtract(image4, image3)

		#image = rslt_fc['img']
			
		#show_image(image, "matching")
		#show_video(image, "matching")
		#show_image(image2, "matching2")
		#show_video(image2, "matching2")		
		#show_image(image3, "matching3")
		#show_video(image3, "matching3")
		#show_image(image4, "matching4")
		show_image(image5, "matching5")

		
		c = cv2.waitKey(10)

		if 'q' == chr(c & 255):
			cv2.destroyAllWindows()			
			break
			output.close()


