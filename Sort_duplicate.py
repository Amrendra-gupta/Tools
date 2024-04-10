import os
from PIL import Image
import imagehash

def find_duplicate_images(folder_path):
    hash_dict = {}
    
    for filename in os.listdir(folder_path):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            path = os.path.join(folder_path, filename)
            img = Image.open(path)
            img_hash = str(imagehash.average_hash(img))
            
            if img_hash in hash_dict:
                hash_dict[img_hash].append(path)
            else:
                hash_dict[img_hash] = [path]
    
    duplicate_images = [v for v in hash_dict.values() if len(v) > 1]
    
    return duplicate_images

'''
This code should be placed in working folder where you want to find duplicates.
Or modify the folder_path variable as per usages.
NOTE: This code may not always return true duplicates, so always review duplicates.
But works good.
'''

print("Put the code in where you want to find duplicate images.\n")
# Example usage
folder_path = '.'
duplicate_images = find_duplicate_images(folder_path)

for group in duplicate_images:
    print("Duplicate images: ", group)
input()
