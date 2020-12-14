import numpy as np
import cv2
import signal
import psychopy
import scipy

def idealLowpassFilter(emptymask, cutoff):
    # mask = None
    # kernel = np.ones((5, 5), np.float32) / 25
    # mask = cv2.filter2D(emptymask, -1, kernel)
    mask = cv2.blur(emptymask, (1,1))
    return mask


def idealHighpassFilter(emptymask, cutoff):
    mask = None
    return mask


def gaussianLowpassFilter(emptymask, cutoff):
    mask = cv2.GaussianBlur(emptymask, (1,1), cutoff)
    return mask


def gaussianHighpassFilter(emptymask, cutoff):
    # mask = cv2.GaussianBlur(emptymask, (3,3), cutoff, borderType=cv2.BORDER_CONSTANT)
    mask = cv2.GaussianBlur(emptymask, (1, 1), cutoff)
    return mask


def butterworthLowpassFilter(emptymask, cutoff, order):
    # mask = None
    # mask = psychopy.filters.butter2d_lp(emptymask, cutoff, order)
    # mask = scipy.signal.butter(emptymask, cutoff, order)

    b, a = signal.butter(order, cutoff, btype='low')
    mask = signal.filtfilt(b, a, emptymask)

    return mask


def butterworthHighpassFilter(emptymask, cutoff, order):
    # mask = None
    b, a = signal.butter(order, cutoff, btype='high', analog=False)
    mask = signal.filtfilt(b, a, emptymask)

    return mask


def ringLowpassFilter(emptymask, cutoff, thickness):
    mask = None
    return mask


def ringHighpassFilter(emptymask, cutoff, thickness):
    mask = None
    return mask
