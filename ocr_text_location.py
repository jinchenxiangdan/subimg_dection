import cv2
import pytesseract 
import glob
import numpy as np
# import imutils

#
# Author: Shawn Jin
#


# set up tesseract (*ONLY* need when using Windows)
pytesseract.pytesseract.tesseract_cmd = r'I:\\Tesseract\\tesseract.exe'

# 
img = cv2.imread('resources\\test_img_1.png')
cv2.imshow("img",img)

###
# Pytesseract
###
# text = pytesseract.image_to_string(img)
# print(text)

# box = pytesseract.image_to_boxes(img)
# print(box)




###
# cv2.matchTemplateTrick
###

# handle the template img
template_img = cv2.imread('resources\\building1_roof.png')
template_gray_img = cv2.cvtColor(template_img, cv2.COLOR_BGR2GRAY)
detect = cv2.Canny(template_gray_img, 50, 200)
(tH, tw) = detect.shape[:2]
cv2.imshow("eg", detect)

#
# loop over the images to find the template in
for imagePath in glob.glob(args["images"] + "/*.jpg"):
	# load the image, convert it to grayscale, and initialize the
	# bookkeeping variable to keep track of the matched region
	image = cv2.imread(imagePath)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	found = None
	# loop over the scales of the image
	for scale in np.linspace(0.2, 1.0, 20)[::-1]:
		# resize the image according to the scale, and keep track
		# of the ratio of the resizing
		resized = imutils.resize(gray, width = int(gray.shape[1] * scale))
		r = gray.shape[1] / float(resized.shape[1])
		# if the resized image is smaller than the template, then break
		# from the loop
		if resized.shape[0] < tH or resized.shape[1] < tW:
			break











# hold img showing
cv2.waitKey(0)
cv2.destroyAllWindows()










