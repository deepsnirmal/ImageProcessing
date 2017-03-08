import time 
import os 

def captureImage() :
	# uses Fswebcam to take picture
	os.system('fswebcam -r 720x12780 -S 3 --jpeg 50 --save /home/deepnirmal/Documents/ImageProcessing/resources/mainImage.jpg') 

	# this line creates a 15 second delay before repeating the loop
	time.sleep(2) 


