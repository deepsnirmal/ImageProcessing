# ImageProcessing
## Introduction
Its a package for sky-lamp project that handles entire image processing.
It helps in capturing the HD image from the webcame of the Document and storing it in a ```resource``` folder. Just after the capturing the image is send to cropping tool name **Document Scanner** that crops the image based on various factors likes binarization, contour lines and gaussian blur formula which gives the ouput as ```croppedImage.jpg```. Further more the same cropped image is being send to **ocropy** image processing library for text extraction and further processing. At last the ```output``` folder will contain a text file holding all the extracted text with 80% efficiency. 

## Environmenmt and Requirements
Install the required packages by using the following commands -
Common :
```sudo apt-get update
sudo apt-get install python-opencv libopencv-dev python-numpy python-dev
```
For document scanner :
```
sudo apt-get install build-essential cython 
sudo apt-get install python-skimage
sudo apt install python-pip
pip install --upgrade pip
pip install -U scikit-image
```
For Ocropy :
```
sudo apt-get install $(cat PACKAGES)
```
## Usage

First set the ```sys.path``` in the ```imageProcessing.py``` file to your current project directory 
```
sys.path.append('/home/deepnirmal/Documents/ImageProcessing/document-scanner')
```

### STEP 1 : Capturing image from the webcam
Import Document-Scanner module
```
import documentScanner as docScan
```
Call the method ```cropImage``` with the path to image that needs to be cropped
```
docScan.cropImage(<imageFolderPath>)
```
### STEP 2 : Extracting text from the binarized image
Import the ocropy library
```
import ocropy as ocr
```

