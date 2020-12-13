# Use this file as you wish to generate the images needed to answer the report

import numpy as np
import cv2

def cartesianPattern(mask_size, percent):
    row, col = mask_size
    mask = np.zeros(mask_size)
    new_percent = percent*row
    line_spacing = int(row/new_percent)
    for x in range(row):
        if(x%line_spacing == 0):
            mask[x,:] = 1

    counter = 0
    for y in range(0, len(mask)):
        if mask[y, 0] == 1:
            counter = counter + 1
            print(y)
    print(str(counter) + " lines with 1's in basic")
    return mask

masking = (1000,1000)
percentage = 0.01

print(cartesianPattern(masking, percentage))