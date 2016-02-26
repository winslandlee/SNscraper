# StanceNationScraper

Web scraper that searches through source code to search for image links.
Uses few plugins such as BeautifulSoup4 and Requests to read HTML source code

saveImage() iterates through links in queue and downloads them to current director assigned by the function createFolder()
createFolder() asks for a folder name and checks if one exists, if not create a new path in set current director

lines 36-38
  searches through source code to find links in corresponding tag using BeautifulSoup4s built in findAll function.
  
Increase download speed of images by implementing multithreading into program by passing in saveImage()

Program is in a while loop in case user has multiple links they want to download from. 
