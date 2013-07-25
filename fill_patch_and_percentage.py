#!/usr/bin/python
from PIL import Image, ImageFont, ImageDraw
import sys
import os
import pdb

im = Image.new('CMYK', (960,480), (0, 0, 0, 0))
font = ImageFont.truetype(("arial.ttf"), 10)
draw = ImageDraw.Draw(im)

x = 0
y = 0

for i in range(256):
    #pdb.set_trace()
    #print i
    img = Image.new('CMYK', (29,29), (0, 0, 0, i))
    if x < 32:
        im.paste(img,(x*30, y*60))
        draw.text((x*30, y*60+30), str(i), font=font)
        draw.text((x*30, y*60+40), str(round(i*100/255.0,1)), font=font)
        im.save("img.tif")
        #print i, x, y
    else:
        x = 0
        y = y+1
        im.paste(img,(x*30, y*60))
        draw.text((x*30, y*60+30), str(i), font=font)
        draw.text((x*30, y*60+40), str(round(i*100/255.0,1)), font=font)
        im.save("img.tif")
        #print i, x, y
    x = x+1
