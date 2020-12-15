# Use this file as you wish to generate the images needed to answer the report

import src.project.Utilities as util
import src.project.SelectiveImageAcquisition as sia
import cv2

heart = "images/cardiac.jpg"
brain = "images/brain.png"

##############  Utilities   ###################
img2 = util.loadImage(heart)
img = util.loadImage(brain)
#util.displayImage(img)
h = img2.shape[0]
w = img2.shape[1]
h1 = img.shape[0]
w1 = img.shape[1]

mask_size = (h, w)
mask_size2 = (h1, w1)

# #######    Part 1&2    #############
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


#################  Part 3  #####################

img_copy2 = util.getDFT(img)

#mask_size2 = (h, w)
percent = .5

mask = sia.cartesianPattern(mask_size2, percent)

mask1 = sia.cartesianPattern(mask_size2, .05)
mask2 = sia.cartesianPattern(mask_size2, .15)
mask3 = sia.cartesianPattern(mask_size2, .35)
mask4 = sia.cartesianPattern(mask_size2, .64)


masks = (mask1, mask2, mask3, mask4)

count = 0
for mask in masks:
    a = util.applyMask(img_copy2, mask)
    b = util.writableDFT(a)
    c = util.normalizeImage(b)
    d = util.post_process_image(c)
    count += 1
    print(count)
    util.displayImage(d)

##############  Part 4  #####################

#change img(heart) to img2(brain)
# img_copy = util.getDFT(img2)
# rays = (1, 15, 50, 100, 360)
#
# mask = sia.radialPattern(mask_size2, rays[0])
#
# mask1 = sia.radialPattern(mask_size2, rays[1])
# mask2 = sia.radialPattern(mask_size2, rays[2])
# mask3 = sia.radialPattern(mask_size2, rays[3])
# mask4 = sia.radialPattern(mask_size2, rays[4])
#
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


###############   Part 5    #################

