from PIL import Image
import os

path = 'your local path'
entries = os.listdir(path)
# Sort file for their name
entries.sort(key=lambda f: str(filter(str, f)))
img_list = []
img_to_merge = set
for entry in entries:
    full_path = path + entry
    img_to_merge = Image.open(full_path)
    img_to_merge.convert('RGB')
    img_list.append(img_to_merge)
# Merge the image list
img_to_merge.save(path + 'jpg_image_to_pdf_format.pdf', save_all=True, append_images=img_list)
 
print('Merge Complete!')