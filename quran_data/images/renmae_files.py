import os 

def rename():
    folders = os.listdir('./')
    for folder in folders:
        if os.path.isdir(folder) and folder != "1":
            folder_path = f"./{folder}/"
            files = os.listdir(folder_path)
            for  i , file in enumerate(files):
                old_path = os.path.join(folder_path, file)
                new_path = os.path.join(folder_path, f"{i+1}{os.path.splitext(file)[1]}")
                os.rename(old_path , new_path)
        else:
            pass       
        
if __name__ =="__main__":
    rename()