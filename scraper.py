from getLinks import getLinks
from saveImages import saveImage

start = True
while(start):
    link = raw_input("What link do you want to download images from?\n")
    #input link needs to have "http://" or it will not work, if statement adds if it does not contain
    if "http://" not in link:
        link = "http://" + link
    url = getLinks(link)
    saveImage(url)
    print ("All Images Downloaded")

    again = raw_input("\nDo you want to download from another link? (y/n)\n")
    if (again == "y"):
        start = True
    elif (again == "n"):
        raise SystemExit

