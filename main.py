#Organize already available files into their necessary folders

#Make sure to stick to files which will not affect the Operating System
##Check type of file it is
#Simple selections: Music,Pictures,Documents,Videos,Archives,
#Desktop Cleanup
#Downloads Cleanup
#Miscellaneous
#Backup Folder
#Automatically sense and place new downloads into set folders

import os
import shutil
print(os.getcwd())


def organize_files(source_dir,target_dir):
    # Create target folders if they don't exist
    target_folders = ['Documents', 'Pictures', 'Music', 'Videos', 'Others','Archives']
    for folder in target_folders:
        os.makedirs(os.path.join(target_dir, folder), exist_ok=True)
        print(f"{folder} created")

    # Get a list of all files in the source directory
    files = os.listdir(source_dir)
    if not files:
        print("Source directory is empty.")
    else:
        print(f"Source directory contains {len(files)} files.")

    for file_name in files:
        file_name_path = os.path.join(source_dir,file_name)
        extension = os.path.splitext(file_name)[1].lower()
        #Documents

        if extension in ['.txt', '.doc', '.docx', '.pdf']:
            source_path = file_name_path
            destination_path = os.path.join(target_dir,"Documents")
            shutil.move(source_path,destination_path)
            directory,base_name = os.path.split(file_name)
            print(f"{base_name} moved to Documents")
        #Pictures
        elif extension in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.tif', '.tiff']:
            source_path = file_name_path
            destination_path = os.path.join(target_dir, "Pictures")
            shutil.move(source_path, destination_path)
            directory, base_name = os.path.split(file_name)
            print(f"{base_name} moved to Pictures")
        #Music
        elif extension in ['.mp3', '.wav', '.ogg', '.flac', '.aac', '.wma']:
            source_path = file_name_path
            destination_path = os.path.join(target_dir, "Music")
            shutil.move(source_path, destination_path)
            directory, base_name = os.path.split(file_name)
            print(f"{base_name} moved to Music")
        #Videos
        elif extension in ['.mp4', '.avi', '.mkv', '.wmv', '.mov', '.flv', '.webm']:
            source_path = file_name_path
            destination_path = os.path.join(target_dir, "Videos")
            shutil.move(source_path, destination_path)
            directory, base_name = os.path.split(file_name)
            print(f"{base_name} moved to Videos")
        #Archives
        elif extension in ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2']:
            source_path = file_name_path
            destination_path = os.path.join(target_dir, "Archives")
            shutil.move(source_path, destination_path)
            directory, base_name = os.path.split(file_name)
            print(f"{base_name} moved to Archives")
        #Others
        else:
            source_path = file_name_path
            destination_path = os.path.join(target_dir, "Others")
            shutil.move(source_path, destination_path)
            directory, base_name = os.path.split(file_name)
            print(f"{base_name} moved to Others")

src = os.path.join(os.getcwd(),"SourceDir")
target = os.path.join(os.getcwd(),"Target")

organize_files(src,target)