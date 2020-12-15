# Use this file as you wish to generate the images needed to answer the report

import src.project.Utilities as util
import src.project.ImageSynthesisNoise as isn


heart = "images/cardiac.jpg"
brain = "images/brain.png"
matrix = "images/noisyimage.npy"

##############  Utilities   ###################
img = util.loadImage(heart)
img2 = util.loadImage(brain)
img3 = util.loadMatrix(matrix)
# util.displayImage(img)
# util.displayImage(img2)
#util.displayImage(img)
h = img.shape[0]
w = img.shape[1]
h1 = img2.shape[0]
w1 = img2.shape[1]

w2 = img3.shape[1]
h2 = img3.shape[0]

print(h2)
print(w2)

mask_size = (h, w)
mask_size2 = (h1, w1)

#img_copy = util.getDFT(img2)

#############  Part 6   ####################
# cutout = (10, 20, 35, 65)
# order = 1
#
# img_copy = util.getDFT(img2)
#
# count = 0
# for cut in cutout:
#     print(cut)
#     mask = isn.butterworthLowpassFilter(mask_size2, cut, 4)
#     a = util.applyMask(img_copy, mask)
#     b = util.writableDFT(a)
#     c = util.normalizeImage(b)
#     d = util.post_process_image(c)
#     count += 1
#     print(count)
#     util.displayImage(d)

###########   Part 7   ######################
# print(w1)
# print(h1)
# cutout = (250, 200, 150, 100)
# count = 0
# for cut in cutout:
#     print(cut)
#     mask = isn.gaussianHighpassFilter(mask_size2, cut)
#     a = util.applyMask(img_copy, mask)
#     b = util.writableDFT(a)
#     c = util.normalizeImage(b)
#     d = util.post_process_image(c)
#     count += 1
#     print(count)
#     util.displayImage(d)

nmask_size = (h2, w2)

img_copy = util.getImage(img3)

mask = isn.idealHighpassFilter(nmask_size, 100)
mask1 = isn.idealLowpassFilter(nmask_size, 100)
mask2 = isn.gaussianHighpassFilter(nmask_size, 100)
mask3 = isn.ringLowpassFilter(nmask_size, 100, 10)
mask4 = isn.butterworthHighpassFilter(nmask_size, 50, 2)

masks = (mask, mask1, mask2, mask3, mask4)

count = 0
for mask in masks:
    a = util.applyMask(mask, img_copy)
    count += 1
    print(count)
    util.displayImage(a)
