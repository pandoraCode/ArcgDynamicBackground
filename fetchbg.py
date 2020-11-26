## Importing Necessary Modules
import requests
import shutil 
import os
import subprocess
from random import seed
from random import randint
import pathlib
import os.path
from os import path



BUCKET_PATH = "https://dynamicbgarch.s3.amazonaws.com/"
CURRENT_DIR = str(pathlib.Path().absolute())






def retrieve_bg(id):



    if not bg_exists(id):

        image_url = BUCKET_PATH+ id+".jpg"
        filename = image_url.split("/")[-1]
        r = requests.get(image_url, stream = True)

        if r.status_code == 200:
            # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
            r.raw.decode_content = True
            
            # Open a local file with wb ( write binary ) permission.
            path = "bg_images/"+filename
            with open(path,'wb') as f:
                shutil.copyfileobj(r.raw, f)
                
            setBg(path)
        else:
            print('Image Couldn\'t be retreived')
    else:
         setBg("/bg_images/"+str(id)+".jpg" )


def executeCommand(commad):
        proc = subprocess.Popen(["pacman -Qs feh "], stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        return out;


def isInstalledFeh():
    isInstalled = "pacman -Qs feh "
    install = "pacman -S feh"

    check = executeCommand(isInstalled)

    if not check : 
        install= executeCommand(install)
        if install:
            return True
        else:
            return False
    return True



def get_random():
        # seed(1)
        # for _ in range(10):
        #     value = randint(0, 10)
        #     return value
        return randint(1, 10)

def bg_exists(id):
    if path.exists(CURRENT_DIR+"/bg_images/"+str(id)+".jpg"):
        return True
    else:
        return False

     
def setBg(bg_img):
    path = CURRENT_DIR+"/" +bg_img
    print(path)
    os.system("feh --bg-scale "+ path)





def bg():
    id = get_random()
    retrieve_bg(str(id))







if __name__ == '__main__':
    bg()