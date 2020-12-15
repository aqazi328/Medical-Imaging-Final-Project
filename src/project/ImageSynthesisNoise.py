import numpy as np
import cv2
import signal

def idealLowpassFilter(emptymask, cutoff):
    row, col = emptymask
    xrow, ycol = row/2, col/2
    lp_mask = np.zeros((row, col), np.float64)

    for i in range(lp_mask.shape[0]):
        for k in range(lp_mask.shape[1]):
            pt = np.sqrt((np.square(i - xrow)) + np.square(k - ycol))
            if pt <= cutoff:
                lp_mask[i][k] = 255
            else:
                lp_mask[i][k] = 0

    mask = lp_mask

    return mask


def idealHighpassFilter(emptymask, cutoff):
    hp_mask = idealLowpassFilter(emptymask, cutoff)
    hp_mask = 255 - hp_mask
    mask = hp_mask

    return mask


def gaussianLowpassFilter(emptymask, cutoff):
    row, col = emptymask
    xrow, ycol = row/2, col/2
    gausLP_mask = np.zeros(emptymask)

    for i in range(row):
        for k in range(col):
            pt = np.sqrt(((i - xrow) * (i - ycol)) + ((k - ycol) * (k - ycol)))
            gausLP_mask[i][k] = np.exp((-1 * np.power(pt, 2)) / (2 * cutoff * cutoff))

    mask = gausLP_mask
    return mask


def gaussianHighpassFilter(emptymask, cutoff):
    gausHL_mask = gaussianLowpassFilter(emptymask, cutoff)
    gausHL_mask = 255 - gausHL_mask
    mask = gausHL_mask

    return mask


def butterworthLowpassFilter(emptymask, cutoff, order):
    row, col = emptymask
    xrow, ycol = row/2, col/2
    bwLP_mask = np.zeros(emptymask)

    for i in range(row):
        for k in range(col):
            pt = np.sqrt(np.power((i - xrow), 2) + np.power((k - ycol), 2))
            bwLP_mask[i][k] = 1/(1 + np.power((pt/cutoff), (2 * order)))

    mask = bwLP_mask

    return mask


def butterworthHighpassFilter(emptymask, cutoff, order):
    bwHP_mask = butterworthLowpassFilter(emptymask, cutoff)
    bwHP_mask = 255 - bwHP_mask
    mask = bwHP_mask

    return mask


def ringLowpassFilter(emptymask, cutoff, thickness):
    row, col = emptymask
    xrow, ycol = row/2, col/2
    rLP_mask = np.zeros(emptymask)

    for i in range(rLP_mask.shape[0]):
        for k in range(rLP_mask.shape[1]):
            pt = np.sqrt((np.square(i - xrow)) + np.square(k - ycol))
            if (pt <= cutoff+thickness) and (pt > (cutoff-thickness)):
                rLP_mask[i][k] = 255
            else:
                rLP_mask[i][k] = 0

    mask = rLP_mask

    return mask


def ringHighpassFilter(emptymask, cutoff, thickness):
    row, col = emptymask
    xrow, ycol = row/2, col/2
    rHP_mask = np.zeros(emptymask)

    for i in range(rHP_mask.shape[0]):
        for k in range(rHP_mask.shape[1]):
            pt = np.sqrt((np.square(i - xrow)) + np.square(k - ycol))
            if (pt > cutoff + thickness) and (pt <= (cutoff - thickness)):
                rHP_mask[i][k] = 0
            else:
                rHP_mask[i][k] = 255

    mask = rHP_mask

    return mask
