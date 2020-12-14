# Use this file as you wish to generate the images needed to answer the report

import numpy as np
import cv2
import math

#def radialPattern(mask_size, ray_count):
def bandPattern(mask_size, width, length, angle):
    mask = None

    row, col = mask_size
    mask = np.zeros(mask_size)
    ang = -angle*math.pi/180
    s = np.sin(ang)
    c = np.cos(ang)

    #Center of image
    center = int(row/2), int(col/2)
    cx = int(row/2)
    cy = int(col/2)
    w = abs(width)
    l = length

    tl_x = (0-l / 2)
    tl_y = (0-w / 2)
    ntl_x = (tl_x * c - tl_y * s) + cy
    ntl_y = (tl_x * s + tl_y * c) + cx

    tr_x = (0 + l / 2)
    tr_y = (0 - w / 2)
    ntr_x = (tr_x * c - tr_y * s) + cy
    ntr_y = (tr_x * s + tr_y * c) + cx

    bl_x = (0 - l / 2)
    bl_y = (0 + w / 2)
    nbl_x = (bl_x * c - bl_y * s) + cy
    nbl_y = (bl_x * s + bl_y * c) + cx

    br_x = (0 + l / 2)
    br_y = (0 + w / 2)
    nbr_x = (br_x * c - br_y * s) + cy
    nbr_y = (br_x * s + br_y * c) + cx

    contours = np.array([[int(ntl_x), int(ntl_y)], [int(ntr_x), int(ntr_y)], [int(nbr_x), int(nbr_y)], [int(nbl_x), int(nbl_y)]])
    cv2.fillPoly(mask, pts=[contours], color=1)

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
w = 10
l = 500
a = 10


print(bandPattern(masking, w, l, a))

# if(angle > 0):
#         rotated_x = int(math.cos(angle) * (x - center[0]) - math.sin(angle) * (y - center[1]) + center[1])
#         rotated_y = int(math.sin(angle) * (x - center[0]) + math.cos(angle) * (y - center[1]) + center[1])
#         new_startP = (rotated_x, rotated_y)
#
#         rotated_x2 = int(math.cos(angle) * (x2 - center[0]) - math.sin(angle) * (y2 - center[1]) + center[1])
#         rotated_y2 = int(math.sin(angle) * (x2 - center[0]) + math.cos(angle) * (y2 - center[1]) + center[1])
#         new_endP = (rotated_x2, rotated_y2)
#
#     # if(angle > 0):
#     #     start_point = int((start_point[1] - center[0]) * math.cos(angle) + (start_point[0] - center[0]) * math.sin(angle) + center[0]), int((start_point[1] - center[1]) * math.sin(angle) - (start_point[0] - center[1]) *math.cos(angle) + center[1])
#     #     end_point = int((end_point[1] - center[0]) * math.cos(angle) + (end_point[0] - center[0]) * math.sin(angle) + center[0]), int((end_point[1] - center[1]) * math.sin(angle) - (end_point[0] - center[1]) *math.cos(angle) + center[1])
#     #     print(start_point)
#     #     print(end_point)
#     #mask = cv2.line(mask, new_startP, new_endP, color=1)