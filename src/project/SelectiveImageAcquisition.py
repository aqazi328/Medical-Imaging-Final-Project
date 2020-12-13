
##
# Objective: Simulate different types of acquisition patterns by implementing the
# following functions.
##

import numpy as np
import cv2


def cartesianPattern(mask_size, percent):
    row, col = mask_size
    mask = np.zeros(mask_size)
    new_percent = percent * row
    line_spacing = int(row/new_percent)
    for x in range(row):
        if (x % line_spacing == 0):
            mask[x, :] = 1
    return mask


def circlePattern(mask_size, radius):
    row, col = mask_size
    maks = np.zeros(mask_size)
    center = int(row/2), int(col/2)
    Y, X = np.ogrid[:row, :col]
    dist_from_center = np.sqrt((X - center[0])**2 + (Y - center[1])**2)
    mask = dist_from_center <= radius
    return mask


def ellipsePattern(mask_size, major_axis, minor_axis, angle):
    mask = None
    return mask


def bandPattern(mask_size, width, length, angle):
    mask = None
    return mask


def radialPattern(mask_size, ray_count):
    mask = None
    return mask


def spiralPattern(mask_size, sparsity):
    mask = None
    return mask
