from PIL import Image
import os

print("Resizes images in a folder to 640*640, overwrites original files, "+ 
    "and saves them with sequential numbering (e.g., 1.jpg, 2.jpg, ...).")
print("")
def resize_and_save_images(folder_path, quality=98):
    """
    Resizes images in a folder to 640*640, overwrites original files, and saves them with
    sequential numbering (e.g., 1.jpg, 2.jpg, ...).
    """

    if not os.path.exists(folder_path):
        raise ValueError(f"Input folder '{folder_path}' does not exist.")

    if not os.listdir(folder_path):
        raise ValueError(f"Input folder '{folder_path}' is empty.")

    file_count = 1
    for filename in os.listdir(folder_path):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            try:
                image_path = os.path.join(folder_path, filename)
                img = Image.open(image_path)
                img_resized = img.resize((640, 640), Image.LANCZOS)
                img_resized.save(os.path.join(folder_path, f"{file_count}.jpg"), quality=quality)
                print(f"Image '{filename}' resized and saved as '{file_count}.jpg'.")
                file_count += 1
            except IOError as e:
                print(f"Error processing '{filename}': {e}")

if __name__ == "__main__":
    folder_path =  input("Please input the folder : ")
    resize_and_save_images(folder_path)

input('enter')
