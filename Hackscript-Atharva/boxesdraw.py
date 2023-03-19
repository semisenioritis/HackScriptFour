import cv2
import pytesseract
from pytesseract import Output
# to make csv file
import pandas as pd
all_words = []
all_coords = []
box_no = []
img = cv2.imread('0000062.png')

d = pytesseract.image_to_data(img, output_type=Output.DICT)
# print(d)
# print(d.keys())
n_boxes = len(d['text'])

def relu():
    sum=0
    for i in range (n_boxes):
        relu=  max(0, int(d['conf'][i]))
        sum= sum+relu

    sum= sum//n_boxes
    # print(sum)
    return sum


for i in range(n_boxes):
    if int(d['conf'][i]) > relu():
        all_words.append(d['text'][i])
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        temp_dict = {
            1:(x,y),
            2:(x+w,y),
            3:(x,y+h),
            4:(x+w,y+h),
        }
        all_coords.append(temp_dict)
csv_dict = {"Text Content":all_words,"Text Coordinates":all_coords}
df = pd.DataFrame(csv_dict)
df.to_csv("test2.csv")
# cv2.imshow('img', img)
# cv2.waitKey(0)


    # for i in range(n_boxes):
    #     if int(d['conf'][i]) >sum:
    #         (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
    #         img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
