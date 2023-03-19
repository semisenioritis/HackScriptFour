import cv2
import pytesseract
import numpy as np

# Load the invoice image
img = cv2.imread('000103.png')


# Preprocess the image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]

# Find contours in the image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Filter contours based on size and aspect ratio
min_area = 1000
max_ratio = 2
valid_contours = []
for contour in contours:
    area = cv2.contourArea(contour)
    x,y,w,h = cv2.boundingRect(contour)
    aspect_ratio = float(w)/h
    if area > min_area and aspect_ratio < max_ratio:
        valid_contours.append(contour)

# Find the contour with the largest area
largest_contour = max(valid_contours, key=cv2.contourArea)

# Get the bounding box coordinates of the largest contour
x,y,w,h = cv2.boundingRect(largest_contour)
x2, y2 = x + w, y + h

# Draw a rectangle around the largest contour
cv2.rectangle(img, (x, y), (x2, y2), (0, 255, 0), 2)

# Display the image
cv2.imshow('image', img)
cv2.imwrite('table.png', img)