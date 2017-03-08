#Importing document scanner and cropping tool from the package
import sys
sys.path.append('/home/deepnirmal/Documents/ImageProcessing/document-scanner')
sys.path.append('/home/deepnirmal/Documents/ImageProcessing/imageCapture')

import documentScanner as docScan
import imageCapture as click
imageFolderPath="resources/"

#Code for Capturing the image and storing it in the document-scanner/images folder
print("###################### Capturing the Image ######################")

click.captureImage();
print("LOG--> Image captured")
print("LOG--> Saved as mainImage.jpg")

print("###################### Croppping the Image ######################")

#Hard coded the file name, can also take from the user or directly from the camera
docScan.cropImage(imageFolderPath+"mainImage.jpg")

print("LOG--> Image cropped ")
print("LOG--> Image Saved as croppedImage.jpg")

