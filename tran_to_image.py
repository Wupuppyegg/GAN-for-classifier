import os
from PIL import Image

filename = os.listdir("root1")
base_dir = "root1"
new_dir = "root2"
#size_m = 640
#size_n = 480
size_m = 640
size_n = 480

for img in filename:
    image = Image.open(base_dir + img)
    if image.mode == "P":
        image = image.convert('RGB')

    image = image.split()[0]
    image_size = image.resize((size_m, size_n), Image.ANTIALIAS)
    image_size.save(new_dir + img)
    print('已存好')
