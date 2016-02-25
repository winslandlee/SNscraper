import requests
from bs4 import BeautifulSoup

pages = 0

def getPages(soup):
    global pages
    ind = str(soup).find('class="cb-page"')
    while ind != -1:
        ind = str(soup).find('class="cb-page"', ind + 1)
        pages += 1
    return int(pages)

def addQueue(soup, queue):
    for image in soup.findAll('a', href=True):            
        if '/uploads/' in image['href']:
            queue.put(image['href'])    

def imageParse(url, soup, queue):
    
    if pages > 0:
        for i in range( 1,pages + 1):
            soup2 = updateLink(url, i)
            addQueue(soup2, queue)    
    else:
        
        addQueue(soup, queue)
        
def updateLink(url, i):
    website = url[:len(url)-1]
    web = "{0}/{1}/".format(website, i)
    response = requests.get(web)
    data = response.text
    soup = BeautifulSoup(data, "html.parser")
    return soup