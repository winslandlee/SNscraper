import requests, Queue, os, getpass, urllib
from threading import Thread
from bs4 import BeautifulSoup

def saveImage(queue):
    index = 1
    size = queue.qsize()
    while not queue.empty():
        print ("Downloading [{}/{}]".format(index, size))
        image = queue.get()
        urllib.urlretrieve(image, os.path.basename(image))
        index += 1
        
def createFolder():
    folderName = raw_input("What do you want to call your folder Name? ")
            #creates folder if it does not exist
    if os.path.exists("C:\Users\\" + getpass.getuser() + "\Pictures\\StanceNation\\" + folderName):
        os.chdir("C:\Users\\" + getpass.getuser() + "\Pictures\\StanceNation\\" + folderName)
    else:
        os.makedirs("C:\Users\\" + getpass.getuser() + "\Pictures\\StanceNation\\" + folderName)
        os.chdir("C:\Users\\" + getpass.getuser() + "\Pictures\\StanceNation\\" + folderName)     

ans = 'y'
while ans == 'y':
    url = raw_input("What is the StanceNation link?\n")
    if 'http://' not in url:
        url = 'http://' + url
        
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")    
    
    queue = Queue.LifoQueue()
    
    createFolder()
    
    for image in soup.findAll('meta', {"property":'og:image'}):            
        if '1140' or '1500' in image['content']:
            queue.put(image['content']) 

    for i in range(10):
        thread_num_1 = Thread(saveImage(queue))
        thread_num_2 = Thread(saveImage(queue)) 
        thread_num_1.start()
        thread_num_2.start()
        
    ans = raw_input("Do you have another link?(y/n)\n") 
sys.exit()
