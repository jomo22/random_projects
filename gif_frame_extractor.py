
import os
from PIL import Image, ImageSequence

gif = Image.open("happy-kid.gif")
# saving each frame as a separate image

os.chdir(r"C:\Users\Josiah\Desktop\School\coding projects\python gif\source images")

for i, frame in enumerate(ImageSequence.Iterator(gif)):
    frame.save(f"frame_{i:02d}.png")
