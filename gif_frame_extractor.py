
import os
from PIL import Image, ImageSequence

gif = Image.open("happy-kid.gif")
# saving each frame as a separate image

os.chdir(r"source images") # change to your source image directory

for i, frame in enumerate(ImageSequence.Iterator(gif)):
    frame.save(f"frame_{i:02d}.png")

