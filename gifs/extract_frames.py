from glob import glob
from PIL import Image
from PIL import GifImagePlugin
import os
from tqdm import tqdm
 
filenames  = glob("*.gif")
subsample = 2
os.mkdir("one_frame_gifs")

for filename in tqdm(filenames):
    dirname = filename.split('.')[0]
    os.mkdir(f"one_frame_gifs/{dirname}")
    img = Image.open(filename)
    frame_number = 1
    for frame in range(0, img.n_frames, subsample):
        img.seek(frame)
        img.save(f"one_frame_gifs/{dirname}/frame_1.png")
        frame_number += 1
        break
