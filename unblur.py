from PIL import Image

import sys


x, y = 1, 2

img = Image.open('secret.png') #Can be many different formats.
pix = img.load()

img_width, img_height = img.size

for h in range(img_height):
    for w in range(img_width):
        r, g, b, a = pix[w, h]
        if all([i > 200 for i in [r, g, b]]):
            sys.stdout.write(' ')
        else:
            sys.stdout.write('.')
    sys.stdout.write('\n')

print img.size #Get the width and hight of the image for iterating over
print pix[x,y] #Get the RGBA Value of the a pixel of an image
# pix[x,y] = value # Set the RGBA Value of the image (tuple)


