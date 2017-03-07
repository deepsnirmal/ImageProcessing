#Importing document scanner and cropping tool from the package
import sys
sys.path.append('/home/deepnirmal/Documents/ImageProcessing/document-scanner')
import documentScanner as docScan

imageFolderPath="document-scanner/images/"


print("###################### Capturing the Image ######################")
#Code for Capturing the image and storing it in the document-scanner/images folder


print("###################### Croppping the Image ######################")

#Hard coded the file name, can also take from the user or directly from the camera
docScan.cropImage(imageFolderPath+"page.jpg")

print("LOG--> Image cropped ")
print("LOG--> Image Saved as Output.jpg")

