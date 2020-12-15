import cv2
import numpy as np


def loadImage(image_path):
    # image = None
    image = cv2.imread(image_path, 0)
    return image


def loadMatrix(filename):
    # matrix = None
    matrix = np.load(filename)
    return matrix


def saveImage(filename, image):
    cv2.imwrite(filename, image)
    return True


def saveMatrix(filename, matrix):
    np.save(filename, matrix)
    return True


# map input image to values from 0 to 255"
def normalizeImage(image):
    normalized = np.zeros((image.shape[0], image.shape[1]))       # not sure if we have to do this or not
    normalized = cv2.normalize(image, normalized, 0, 255, cv2.NORM_MINMAX)
    return normalized


# Remember: the DFT its a decomposition of signals
#  To be able to save it as an image you must convert it.
def writableDFT(dft_image):
    converted = np.fft.ifftshift(dft_image)
    f = np.fft.ifft2(converted)
    image_back = np.abs(f)
    # do this to bring to center and make image easier to see
    # converted = cv2.dft(np.float32(dft_image), flags=cv2.DFT_COMPLEX_OUTPUT)  # its either that^ or this
    return image_back


# Use openCV to display your image"
# Remember: normalize binary masks and convert FFT matrices to be able to see and save them"
def displayImage(image):
    cv2.namedWindow("Image")
    cv2.imshow("Image", image)
    cv2.waitKey()
    cv2.destroyAllWindows()


def getDFT(image):
    f = np.fft.fft2(image)
    dft_shift = np.fft.fftshift(f)
    return dft_shift

# Convert from fft matrix to an image"
def getImage(dft_img):
    inverse_img = np.fft.ifftshift(dft_img)
    f = np.fft.ifft2(inverse_img)
    img_back = np.abs(f)
    return img_back

# Both input values must be raw values"
def applyMask(image_dft, mask):
    return image_dft * mask


def signalToNoise(Arr, axis=0, ddof=0):                                 # need to do
    # return False
    Arr = np.asanyarray(Arr)
    mean = Arr.mean(axis)
    sd = Arr.std(axis=axis, ddof=ddof)
    return np.where(sd == 0, 0, mean/sd)


#[Provide] Use this function to acomplish a good final image
def post_process_image(image):
    a = np.min(image)
    b = np.max(image)
    k = 255
    image = (image - a) * (k / (b - a))
    return image.astype('uint8')
