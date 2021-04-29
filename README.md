# videoscrambler

These 2 scripts can be used to randomly scramble the content of a video. Some example uses would be to overcome ASMR immunity to certain favourite videos where repeated watching + exposure has led to diminishing returns of ASMR. The code relies on ffmpeg to edit the videos and python to scramble. Default scrambling is 5 second chunks.

Instructions:

1) Open VideoSplitter in your IDE of choice (e.g., Spyder). Run the script with command line options filling in the appropriate video file with the full directory and choosing the increments you want in seconds. Eg., to split the P002.mp4 video file into 5s chunks:

# CTRL+F6 with command line options:
# -f "C:\Users\Administrator\Documents\Python\test\P002.mp4" -s 5 -v libx264 

2) Open Shufflevids.py and fill in the dirvid and videoextension vars to match the directory and extension of the video format you want to randomise and concatenate back together. This script will then produce a .txt output of the filenames of all the files created from VideoSplitter.py in a randomised order. Finally the script will concatenate these chunks back together in the randomised order.
