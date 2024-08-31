import os 
import shutil 
from sklearn.model_selection import train_test_split

image_dir = r'C:\Users\BHAVESH\OneDrive\Desktop\Object_Detection\image'
train = r'C:\Users\BHAVESH\OneDrive\Desktop\Object_Detection\image/train'
val = r'C:\Users\BHAVESH\OneDrive\Desktop\Object_Detection\image/val'

# Create the train and validation directories if they don't exist
os.makedirs(train, exist_ok=True)
os.makedirs(val, exist_ok=True)


def split_data(image_path,train_path,val_path):
    image_files = [f for f in os.listdir(image_path) if os.path.isfile(os.path.join(image_path, f))]
    # splitting data with help of train_test_split
    train_files, val_files = train_test_split(image_files, test_size=0.2, random_state=42)
    # Copy image files to the training directory
    for file in train_files:
        shutil.copy(os.path.join(image_path, file), os.path.join(train_path, file))

    # Copy image files to the validation directory
    for file in val_files:
        shutil.copy(os.path.join(image_path, file), os.path.join(val_path, file))

    print(f"Total images: {len(image_files)}")
    print(f"Training images: {len(train_files)}")
    print(f"Validation images: {len(val_files)}")


split_data(image_dir,train,val)