# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 12:55:39 2019

"""
from pathlib import Path

dirVid = Path("C:/Users/Administrator/Documents/Python/test") # set this to your directory where the video is (make sure there is only 1 video with the .mp4 extension in here without a '-' in the name). Make sure slash direction is c
videoextension = 'mp4' # set the video extension here 

import os
import fnmatch
import random
import subprocess

asps = []
for root, dirs, files in os.walk(dirVid):
    asps = fnmatch.filter(files, '*-*.{}'.format(videoextension))
    rootname = set(files).difference(asps)
    rootname = fnmatch.filter(rootname, '*.{}'.format(videoextension))
    rootname = str(rootname)
    rootname = rootname[2:len(rootname)-6]
    
for index, a in enumerate(asps):
    asps[index] = "file '" + root + '\\' + a + "'"
  
random.shuffle(asps)    

print(asps)
randomordertxt = '{}\{}_RandomisedOrder.txt'.format(root, rootname)
randomorderVid = '{}\{}_RandomisedOrder.{}'.format(root, rootname,videoextension)

with open(randomordertxt, 'w') as file_handler:
    for item in asps:
        file_handler.write("{}\n".format(item))
        
# C:\Users\liltimmy\Documents\Python\P002>ffmpeg -f concat -i P000_2.txt -c copy P000_2_Randomized.mp4
        
# ffmpeg -i "P000_1.mp4" -vcodec msmpeg4v3 -b:v 4000K -acodec wmav2 -b:a 192K -aspect 4:3 -s 1280x960 -ss 00:00:00 -to 00:10:00 "Part 1 Vid 1.wmv"

# ffmpeg -i "P002_1_Randomized.mp4" -vcodec msmpeg4v3 -b:v 4000K -acodec wmav2 -b:a 192K -aspect 4:3 -s 1280x960 -ss 00:00:00 -to 00:10:00 "Part 1 Vid 2.wmv"
        
# ffmpeg -i "P000_2.mp4" -vcodec msmpeg4v3 -b:v 4000K -acodec wmav2 -b:a 192K -aspect 4:3 -s 1280x960 -ss 00:00:00 -to 00:10:00 "Part 2 Vid 1.wmv"

# ffmpeg -i "P000_2_Randomized.mp4" -vcodec msmpeg4v3 -b:v 4000K -acodec wmav2 -b:a 192K -aspect 4:3 -s 1280x960 -ss 00:00:00 -to 00:10:00 "Part 2 Vid 2.wmv"
concat_text = "ffmpeg -f concat -safe 0 -i {} -c copy {}".format(randomordertxt, randomorderVid)

subprocess.check_output(concat_text, shell=True)
