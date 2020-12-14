import numpy as np
import cv2
import signal
import psychopy
from scipy.signal import butter, lfilter
from PIL import Image, ImageFilter
from scipy import fftpack
import imageio
from PIL import Image, ImageDraw

def idealLowpassFilter(emptymask, cutoff):
    # kernel = np.ones((cutoff, cutoff), np.float32) / cutoff*cutoff
    # mask = cv2.filter2D(emptymask, 0, kernel)

    # mask = cv2.boxFilter(emptymask, 0, (cutoff, cutoff))

    # mask = cv2.blur(emptymask, (cutoff,cutoff))

    # mask = emptymask.filter(ImageFilter.MinFilter(cutoff))

    # image = cv2.cvtColor(emptymask, cv2.COLOR_BGR2GRAY)
    # mask = cv2.blur(image, (cutoff, cutoff))

    # dft = cv2.dft(np.float32(emptymask), flags=cv2.DFT_COMPLEX_OUTPUT)
    # dft_shift = np.fft.fftshift(dft)
    # mask = 20 * np.log(cv2.magnitude(dft_shift[:, :, cutoff], dft_shift[:, :, cutoff]))

    # mask = cv2.magnitude(emptymask[:, :, cutoff], emptymask[:, :, cutoff])

    mask = None
    return mask


def idealHighpassFilter(emptymask, cutoff):
    # mask = emptymask.filter(ImageFilter.BLUR)

    mask = emptymask.filter(ImageFilter.MaxFilter(cutoff))

    # mask = None
    return mask


def gaussianLowpassFilter(emptymask, cutoff):
    image = cv2.cvtColor(emptymask, cv2.COLOR_BGR2GRAY)
    mask = cv2.GaussianBlur(image, (cutoff, cutoff), 0)
    return mask


def gaussianHighpassFilter(emptymask, cutoff):
    # mask = cv2.GaussianBlur(emptymask, (3,3), cutoff, borderType=cv2.BORDER_CONSTANT)

    # mask = cv2.GaussianBlur(emptymask, (1, 1), cutoff)
    mask = cv2.GaussianBlur(emptymask, (cutoff, cutoff), 0)

    # mask = None
    return mask


def butterworthLowpassFilter(emptymask, cutoff, order):


    # mask = psychopy.filters.butter2d_lp(emptymask, cutoff, order)

    # mask = scipy.signal.butter(emptymask, cutoff, order)

    nyq = 0.5 * 30          # I'm assuming 30 hz?
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    mask = lfilter(b, a, emptymask)

    # mask = None
    return mask


def butterworthHighpassFilter(emptymask, cutoff, order):

    # b, a = signal.butter(order, cutoff, btype='high', analog=False)
    # mask = signal.filtfilt(b, a, emptymask)

    mask = signal.butter(order, emptymask, 'low', analog=True)

    # mask = None
    return mask


def ringLowpassFilter(emptymask, cutoff, thickness):
    mask = None
    return mask


def ringHighpassFilter(emptymask, cutoff, thickness):
    mask = None
    return mask
