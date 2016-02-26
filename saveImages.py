import os
import getpass
import urllib

def saveImage(queue):
    i = 1
    size = queue.qsize()
    while not queue.empty():
        print ("Downloading [{}/{}]".format(i, size))          
        image = queue.get()
        urllib.urlretrieve(image, os.path.basename(image))
        i += 1

def makeDir():
    folderName = raw_input("Folder Name? ")
    
        #creates folder if it does not exist
    if os.path.exists("C:\Users\\" + getpass.getuser() + "\Pictures\\StanceNation\\" + folderName):
        os.chdir("C:\Users\\" + getpass.getuser() + "\Pictures\\StanceNation\\" + folderName)
    else:
        os.makedirs("C:\Users\\" + getpass.getuser() + "\Pictures\\StanceNation\\" + folderName)
        os.chdir("C:\Users\\" + getpass.getuser() + "\Pictures\\StanceNation\\" + folderName)

    