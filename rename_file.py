# This code renames all files endswith(jpg, jpeg, png) in a specified folder with a 
# numeric suffix (e.g. "image1.jpg", "image2.jpg", etc.)

import os

def rename_files(folder_path):
    i = 1
    for filename in os.listdir(folder_path):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            new_filename = str(i) + ".jpg"
            src = os.path.join(folder_path, filename)
            dst = os.path.join(folder_path, new_filename)
            
            try:
                os.rename(src, dst)
                print(f"Renamed {filename} to {new_filename}")
                i += 1
            except Exception as e:
                print(f"Error renaming {filename}: {str(e)}")
                
# Example usage
folder_path = input("Please input the folder to rename : ")
rename_files(folder_path)
input()
