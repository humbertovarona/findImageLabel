# findImageLabel

# Version

1.0

# Release date

December, 2, 2022

# License

MIT

# Description

Check if an image contains a label

# Functions list

- extract_Alllabels: Search all the labels in an image through an OCR
- find_label: Returns "true" if a label is found on an image

# How to install

## import cv2

- Open File > Settings > Project from the PyCharm menu.
- Select your current project.
- Click the Python Interpreter tab within your project tab.
- Click the small + symbol to add a new library to the project.
- Now type in the library to be installed, in your example "opencv-python" without quotes, and click Install Package.

## import pytesseract

- On Linux

sudo apt-get install libleptonica-dev tesseract-ocr libtesseract-dev python3-pil tesseract-ocr-eng tesseract-ocr-script-latn

- On Mac

brew install tesseract

- On Windows

download binary from https://github.com/UB-Mannheim/tesseract/wiki. then add pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe' to your script.

## Install library

- On Linux and Mac

pip install tesseract 

pip install tesseract-ocr

- On Windows

pip install pytesseract 

pip install tesseract

