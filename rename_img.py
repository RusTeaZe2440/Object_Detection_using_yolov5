import os 
import shutil

watch_img = r'C:\Users\BHAVESH\OneDrive\Desktop\Object_Detection\watch'
phones_img = r'C:\Users\BHAVESH\OneDrive\Desktop\Object_Detection\Phones'
file_extension = '.jpg'

for index,image in enumerate(os.listdir(watch_img)):
    current_image_path_watch = os.path.join(watch_img,image)

    if os.path.isfile(current_image_path_watch):
        new_img_name = f'watch{index+1}{file_extension}'
        new_image_path = os.path.join(watch_img,new_img_name)

        os.rename(current_image_path_watch,new_image_path)

print("Renaming Complete for Watch")

for index,phone_img in enumerate(os.listdir(phones_img)):
    current_image_path_phone = os.path.join(phones_img,phone_img)

    if os.path.isfile(current_image_path_phone):
        new_img_name = f'Mobile{index+1}{file_extension}'
        new_image_path = os.path.join(phones_img,new_img_name)

        os.rename(current_image_path_phone,new_image_path)

print("Renaming Complete for Watch")