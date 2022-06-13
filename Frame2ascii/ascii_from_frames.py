import pywhatkit as kt
import os
from image_to_ascii import ImageToAscii
import uuid
import time
import cv2

#============================================================================================================================#
def convert_frames_to_ascii_ImageToAscii(path_frame):
	# path = "C:\\Users\\DucPhan\\Documents\\Python\\Unuse\\frames" 
	list_frame = os.listdir(os.path.expanduser(path_frame))
	FJoin = os.path.join
	files = [FJoin(path_frame, f) for f in os.listdir(path_frame)]

	for i in range(0,33):
		i += 1
		ImageToAscii(imagePath=files[i],outputFile='output frame_ txt\\frame_1.txt')
		time.sleep(0.05)
#============================================================================================================================#



#============================================================================================================================#
def convert_video_to_frame(path, folder_frame):
	vidcap = cv2.VideoCapture(path)
	success,image = vidcap.read()
	count = 0
	success = True
	while success:
		success,image = vidcap.read()
		cv2.imwrite("C:\\Users\\DucPhan\\Documents\\Python\\Unuse\\{}\\frame%d.jpg".format(folder_frame) % count, image)     
		if cv2.waitKey(10) == 27:                     
			break
		count += 1
#============================================================================================================================#


#============================================================================================================================#
def convert_frames_to_ascii_pywhatkit(source_path, target_path):
	# source_path = "C:\\Users\\DucPhan\\Documents\\Python\\Unuse\\output frame"
	# target_path = 'C:\\Users\\DucPhan\\Documents\\Python\\Unuse\\output frame_ txt\\frame'

	list_frame_0 = os.listdir(os.path.expanduser(source_path))
	FJoin = os.path.join
	files_0 = [FJoin(source_path, f) for f in os.listdir(source_path)]

	# list_frame_1 = os.listdir(os.path.expanduser(target_path))
	# FJoin = os.path.join
	# files_1 = [FJoin(target_path, f) for f in os.listdir(target_path)]

	for i in range(0,180):
		i += 1
		kt.image_to_ascii_art(files_0[i], target_path)
		f = open('C:\\Users\\DucPhan\\Documents\\Python\\Unuse\\output frame_ txt\\frame.txt', 'r')
		file_contents = f.read()
		print (file_contents)
#============================================================================================================================#


# convert_video_to_frame(path = "C:\\Users\\DucPhan\\Downloads\\fuk.mp4", folder_frame="output frame 3")
# convert_frames_to_ascii_ImageToAscii(path_frame = "C:\\Users\\DucPhan\\Documents\\Python\\Unuse\\output frame 3")

print("Done")