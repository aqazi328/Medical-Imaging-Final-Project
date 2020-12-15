
##
# Objective: Simulate different types of acquisition patterns by implementing the
# following functions.
##

import numpy as np
import cv2
import math


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
    mask = np.zeros(mask_size)
    center = int(row/2), int(col/2)
    Y, X = np.ogrid[:row, :col]
    dist_from_center = np.sqrt((X - center[0])**2 + (Y - center[1])**2)
    mask = dist_from_center <= radius
    return mask


def ellipsePattern(mask_size, major_axis, minor_axis, angle):
    row, col = mask_size
    mask = np.zeros(mask_size)
    center = int(row/2), int(col/2)
    mask = cv2.ellipse(mask, center, axes=(major_axis, minor_axis), angle=angle, startAngle=0, endAngle=360, color=1, thickness=-1)

    return mask


def bandPattern(mask_size, width, length, angle):
    row, col = mask_size
    mask = np.zeros(mask_size)
    ang = -angle*math.pi/180
    s = np.sin(ang)
    c = np.cos(ang)

    cx = int(row/2)
    cy = int(col/2)
    w = width
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

    return mask


def radialPattern(mask_size, ray_count):
    row, col = mask_size
    mask = np.zeros(mask_size)
    ang = 180 / ray_count
    cx = int(row / 2)
    cy = int(col / 2)

    px = row / 2
    py = 0
    dx = -row / 2
    dy = 0

    for i in range(ray_count):
        angle = ang*i
        s = np.sin(-angle * math.pi / 180)
        c = np.cos(-angle * math.pi / 180)
        x1 = (px * c - py * s) + cx
        y1 = (px * s + py * c) + cy
        x2 = (dx * c - dy * s) + cx
        y2 = (dx * s + dy * c) + cy
        p1 = (int(x1), int(y1))
        p2 = (int(x2), int(y2))
        cv2.line(mask, p1, p2, 1)

    return mask


def spiralPattern(mask_size, sparsity):
    mask = None
    return mask
