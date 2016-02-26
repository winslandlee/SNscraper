# StanceNationScraper

Created by Winsland Lee
On the website "http://www.stancenation.com/" they post images from car events and features. They post a lot of images that can be over 200 photos. Instead of manually saving them, I wanted to create a webscraper that would automatically download images based on a given link. 

I primarily use it for links under the "Event Coverage" tab on the main website.


Web scraper that searches through source code to search for image links.
Uses few plugins such as BeautifulSoup4 and Requests to read HTML source code

saveImage() iterates through links in queue and downloads them to current director assigned by the function createFolder()
createFolder() asks for a folder name and checks if one exists, if not create a new path in set current director

lines 36-38
  searches through source code to find links in corresponding tag using BeautifulSoup4s built in findAll function.
  
Increase download speed of images by implementing multithreading into program by passing in saveImage()

Program is in a while loop in case user has multiple links they want to download from. 
