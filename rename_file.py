
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
folder_path = 'E:/Machine-Learning/Image-Classification-Multi/New/Dataset1/Dataset1/images3 - Copy'
rename_files(folder_path)
input()
