import requests
import Queue
import getLinks
import saveImages
from threading import Thread
from bs4 import BeautifulSoup

queue = Queue.Queue()

url = raw_input("link?\n")
if 'http://' not in url:
    url = 'http://' + url
    
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data, "html.parser")

pages = getLinks.getPages(soup)

saveImages.makeDir()

getLinks.imageParse(url, soup, queue)

for i in range(10):
    thread = Thread(saveImages.saveImage(queue))
    thread.start()

queue.join()

print ("All Images Downloaded")