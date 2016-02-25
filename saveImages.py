import os
import urllib
import getpass

def saveImage(linkArray):

    folderName = raw_input("Folder Name? ")

    #creates folder if it does not exist
    if os.path.exists("C:\Users\\" + getpass.getuser() + "\Pictures\\StanceNation\\" + folderName):
        os.chdir("C:\Users\\" + getpass.getuser() + "\Pictures\\StanceNation\\" + folderName)
    else:
        os.makedirs("C:\Users\\" + getpass.getuser() + "\Pictures\\StanceNation\\" + folderName)
        os.chdir("C:\Users\\" + getpass.getuser() + "\Pictures\\StanceNation\\" + folderName)
    for i in range (0,len(linkArray)):
        print("Downloading [" + str(i + 1) + "/" + str(len(linkArray)) + "]")        
        urllib.urlretrieve(linkArray[i], os.path.basename(linkArray[i]))

