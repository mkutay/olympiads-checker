import cv2
import numpy as np
import pytesseract

def csolver(file):
    img = cv2.imread(file)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ekernel = np.ones((1,2),np.uint8)
    eroded = cv2.erode(gray, ekernel, iterations = 1)
    dkernel = np.ones((2,3),np.uint8)
    dilated_once = cv2.dilate(eroded, dkernel, iterations = 1)
    ekernel = np.ones((2,2),np.uint8)
    dilated_twice = cv2.erode(dilated_once, ekernel, iterations = 1)
    threshed = cv2.adaptiveThreshold(dilated_twice, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 15, 20) # change the second int to 5-15-20 until a correct thing comes
    dkernel = np.ones((2,2),np.uint8)
    threshed_dilated = cv2.dilate(threshed, dkernel, iterations = 1)
    ekernel = np.ones((2,2),np.uint8)
    threshed_eroded = cv2.erode(threshed_dilated, ekernel, iterations = 1)

    cv2.imwrite("temp.jpg", threshed_eroded)
    text = pytesseract.image_to_string(threshed_eroded)
    text = ''.join(text.split())
    print(text)
    return text
