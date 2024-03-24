import os

directory_path = "<SPECIFY FILE PATH>"

def retrieve_image():

    while True:
        files = os.listdir(directory_path)
        if len(files) != 0:
            return directory_path + "/" + files[0]