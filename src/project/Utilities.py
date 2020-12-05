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
    np.save(filename, matrix)
    return True


# map input image to values from 0 to 255"
def normalizeImage(image):
    # normalized = None
    normalized = np.zeros((800, 800))       # not sure if we have to do this or not
    normalized = cv2.normalize(image, normalized, 0, 255, cv2.NORM_MINMAX)
    return normalized


# Remember: the DFT its a decomposition of signals
#  To be able to save it as an image you must convert it.
def writableDFT(dft_image):
    # converted = None
    f = np.fft.fft2(dft_image)
    converted = np.fft.fftshift(f)      # do this to bring to center and make image easier to see
    # converted = cv2.dft(np.float32(dft_image), flags=cv2.DFT_COMPLEX_OUTPUT)  # its either that^ or this
    return converted


# Use openCV to display your image"
# Remember: normalize binary masks and convert FFT matrices to be able to see and save them"
def displayImage(image):
    cv2.namedWindow("Image")
    cv2.imshow("Image", image)
    cv2.waitKey()
    cv2.destroyAllWindows()


def getDFT(image):
    dft_image = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)   # what's the difference between this and writableDFT??
    return dft_image


# Convert from fft matrix to an image"
def getImage(dft_img):                                 # pretty sure this is wrong; using this
    rows, cols = dft_img.shape                     # https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_transforms/py_fourier_transform/py_fourier_transform.html
    crow, ccol = rows / 2, cols / 2
    dft_img[crow - 30:crow + 30, ccol - 30:ccol + 30] = 0
    f_ishift = np.fft.ifftshift(dft_img)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)
    return img_back


# Both input values must be raw values"
def applyMask(image_dft, mask):
    return image_dft * mask


def signalToNoise():                                 # need to do
    return False


#[Provide] Use this function to acomplish a good final image
def post_process_image(image):
    a = np.min(image)
    b = np.max(image)
    k = 255
    image = (image - a) * (k / (b - a))
    return image.astype('uint8')
