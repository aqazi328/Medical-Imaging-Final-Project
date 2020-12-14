# Use this file as you wish to generate the images needed to answer the report

import src.project.Utilities as util
import src.project.SelectiveImageAcquisition as sia
import cv2

heart = "images/cardiac.jpg"
brain = "images/brain.png"

##############  Utilities   ###################
img = util.loadImage(heart)
#util.displayImage(img)
h = img.shape[0]
w = img.shape[1]

mask_size = (h, w)

########    Part 1    #############
# angle = 35
# img_copy = util.getDFT(img)
# mask = sia.bandPattern(mask_size, 10, 50, angle)
# util.displayImage(mask)
#
# mask1 = sia.bandPattern(mask_size, 10, 50, 100)
# mask2 = sia.bandPattern(mask_size, 100, 50, angle)
# mask3 = sia.bandPattern(mask_size, 10, 100, angle)
# mask4 = sia.bandPattern(mask_size, 150, 75, 265)
# #mask = sia.cartesianPattern(mask_size, 50)
# # util.displayImage(mask)
# # util.displayImage(mask1)
# # util.displayImage(mask2)
# # util.displayImage(mask3)
# # util.displayImage(mask4)
# masks = (mask1, mask2, mask3, mask4)
#
# count = 0
# for mask in masks:
#     a = util.applyMask(img_copy, mask)
#     b = util.writableDFT(a)
#     c = util.normalizeImage(b)
#     d = util.post_process_image(c)
#     count += 1
#     print(count)
#     util.displayImage(d)


##################  Part 2  #####################
#
# img_copy2 = util.getDFT(img)
#
# mask_size2 = (h, w)
# percent = .5
#
# mask = sia.cartesianPattern(mask_size2, percent)
#
# mask1 = sia.cartesianPattern(mask_size2, .05)
# mask2 = sia.cartesianPattern(mask_size2, .15)
# mask3 = sia.cartesianPattern(mask_size2, .35)
# mask4 = sia.cartesianPattern(mask_size2, .64)
#
#
# masks = (mask1, mask2, mask3, mask4)
#
# count = 0
# for mask in masks:
#     a = util.applyMask(img_copy2, mask)
#     b = util.writableDFT(a)
#     c = util.normalizeImage(b)
#     d = util.post_process_image(c)
#     count += 1
#     print(count)
#     util.displayImage(d)

##############  Part 3  #####################

img_copy = util.getDFT(img)
