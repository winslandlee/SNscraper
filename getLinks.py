import urllib
from bs4 import BeautifulSoup, SoupStrainer

def getLinks(website):


    linkArray = []

    #finds how many pages of images on website
    soup = getSoup(website)
    pages = getPages(soup)

    print ("Searching for image links...")
    
    #searches all image links in all the pages in link
    for i in range (1, pages):
        index = len(website)
        web = website[:index]
        web = "{0}/{1}/".format(website, i)
        htmltext = urllib.urlopen(web)
        soup2 = BeautifulSoup(htmltext, "html.parser")

        for image in soup2.findAll('a', href=True):
            if '/uploads/' in image['href']:
                linkArray.append(image['href'])
         
    return linkArray


def getSoup(website):
    html = urllib.urlopen(website)
    soup = BeautifulSoup(html, "html.parser")
    return soup

def getPages(soup):
    pages = 0
    ind = str(soup).find('class="cb-page"')
    while ind != -1:
        ind = str(soup).find('class="cb-page"', ind + 1)
        pages += 1
    return int(pages)

def getImageLinks(linkArray, soup):
    for image in soup.findAll('a', href=True):
        if '/uploads/' in image:
            linkArray.append(image['href'])
    