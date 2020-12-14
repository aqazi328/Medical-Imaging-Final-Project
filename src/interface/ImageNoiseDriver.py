# Use this file as you wish to generate the images needed to answer the report

import numpy as np
import cv2

def bandPattern(mask_size, width, length, angle):
    row, col = mask_size
    mask = np.zeros(mask_size)

    #Center of image
    center = int(row/2), int(col/2)
    #start and end points
    start_point = int(center[0] + length/2), int(center[0] - width/2)
    end_point = int(center[0] - length/2), int(center[0] + width/2)
    mask = cv2.rectangle(mask, end_point, start_point, color=1, thickness=-1)

    counter = 0
    for y in range(0, len(mask)):
        if (mask[y, 0] == 1):
            counter += 1
            print(y)
    print(str(counter) + " Number of 1's")

    cv2.imshow('image', mask)
    cv2.waitKey(0)
    return mask

masking = (1000,1000)
w = -5
l = 1000
a = 0


print(bandPattern(masking, w, l, a))