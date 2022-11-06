from PIL import Image
import os

path = 'C:\\Users\\Klaid\\Desktop\\Dalisa\\'
entries = os.listdir(path)
entries.sort(key=lambda f: str(filter(str, f)))
img_list = []
img_to_merge = set
for entry in entries:
    full_path = path + entry
    img_to_merge = Image.open(full_path)
    img_to_merge.convert('RGB')
    img_list.append(img_to_merge)
    #print(full_path)
img_to_merge.save(path + 'korca_images_to_print_2.pdf', save_all=True, append_images=img_list)
 
print('Merge Complete!')