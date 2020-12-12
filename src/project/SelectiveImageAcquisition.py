import numpy as np
import cv2


##
# Objective: Simulate different types of acquisition patterns by implementing the
# following functions.
##

def cartesianPattern(mask_size, percent):
    num_lines = mask_size[1] * percent      # I think mask_size[1] is the pixel height
    mask = None
    return mask


def circlePattern(mask_size, radius):
    mask = None
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
