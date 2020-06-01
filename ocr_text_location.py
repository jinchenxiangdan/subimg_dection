import cv2
import imutils as imutils
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
# img = cv2.imread('resources\\test_img_1.png')
# cv2.imshow("img",img)

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
template_img = cv2.imread('resources\\building2.png')
template_gray_img = cv2.cvtColor(template_img, cv2.COLOR_BGR2GRAY)
detect = cv2.Canny(template_gray_img, 50, 200)
(tH, tW) = detect.shape[:2]
cv2.imshow("eg", detect)

# load the whole img
test_1_img = cv2.imread('resources\\test_2.png')
gray = cv2.cvtColor(test_1_img, cv2.COLOR_BGR2GRAY)
found = None
for scale in np.linspace(0.1, 5.0, 50)[::-1]:
	# resize the image according to the scale, and keep track
	# of the ratio of the resizing
	resized = imutils.resize(gray, width=int(gray.shape[1] * scale))
	r = gray.shape[1] / float(resized.shape[1])
	# if the resized image is smaller than the template, then break
	# from the loop
	if resized.shape[0] < tH or resized.shape[1] < tW:
		break

	# detect edges in the resized, grayscale image and apply template
	# matching to find the template in the image
	edged = cv2.Canny(resized, 50, 200)
	result = cv2.matchTemplate(edged, detect, cv2.TM_CCOEFF)
	(_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)
	# check to see if the iteration should be visualized

	# draw a bounding box around the detected region
	clone = np.dstack([edged, edged, edged])
	cv2.rectangle(clone, (maxLoc[0], maxLoc[1]),
		(maxLoc[0] + tW, maxLoc[1] + tH), (0, 0, 255), 2)
	cv2.imshow("Visualize", clone)
	cv2.waitKey(0)
	# if we have found a new maximum correlation value, then update
	# the bookkeeping variable
	if found is None or maxVal > found[0]:
		found = (maxVal, maxLoc, r)
# unpack the bookkeeping variable and compute the (x, y) coordinates
# of the bounding box based on the resized ratio
(_, maxLoc, r) = found
(startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
(endX, endY) = (int((maxLoc[0] + tW) * r), int((maxLoc[1] + tH) * r))
# draw a bounding box around the detected result and display the image
cv2.rectangle(test_1_img, (startX, startY), (endX, endY), (0, 0, 255), 2)
cv2.imshow("Image", test_1_img)
cv2.resizeWindow("Image", 1080, 560)
# cv2.imshow("Resized Img", cv2.resize(test_1_img, (1080, 540)) )
cv2.waitKey(0)







# hold img showing
cv2.waitKey(0)
cv2.destroyAllWindows()










