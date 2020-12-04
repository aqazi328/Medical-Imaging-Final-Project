import cv2
import numpy as np


def loadImage(image_path):
    # image = None
    image = cv2.imread(image_path)
    return image


def loadMatrix(filename):
    # matrix = None
    matrix = np.loadtxt(filename)
    return matrix


def saveImage(filename, image):
    cv2.imwrite(filename, image)
    return True


def saveMatrix(filename, matrix):
    return True


# map input image to values from 0 to 255"
def normalizeImage(image):
    # normalized = None
    normalized = np.zeros((800, 800))
    normalized = cv2.normalize(image, normalized, 0, 255, cv2.NORM_MINMAX)
    return normalized


# Remember: the DFT its a decomposition of signals
#  To be able to save it as an image you must convert it.
def writableDFT(dft_image):
    converted = None
    return converted


# Use openCV to display your image"
# Remember: normalize binary masks and convert FFT matrices to be able to see and save them"
def displayImage(image):
    cv2.namedWindow("Image")
    cv2.imshow("Image", image)
    cv2.waitKey()
    cv2.destroyAllWindows()


def getDFT(image):
    return None


# Confert from fft matrix to an image"
def getImage(dft_img):
    return None


# Both input values must be raw values"
def applyMask(image_dft, mask):
    return image_dft * mask


def signalToNoise():
    return False


#[Provide] Use this function to acomplish a good final image
def post_process_image(image):
    a = np.min(image)
    b = np.max(image)
    k = 255
    image = (image - a) * (k / (b - a))
    return image.astype('uint8')
