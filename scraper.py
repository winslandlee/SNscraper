import requests
import urllib
import os
from multiprocessing import cpu_count, JoinableQueue, Process
from bs4 import BeautifulSoup


FOLDER_PATH_FORMAT_STRING = "C:\Users\\{}\\Pictures\\StanceNation\\{}"


def get_links(queue):
    url = raw_input("What is the StanceNation link?\n")
    if 'http://' not in url:
        url = 'http://' + url

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    for image in soup.findAll('meta', {"property": 'og:image'}):
        if '1140' or '1500' in image['content']:
            queue.put(image['content'])


def save_image(queue):
    index = 1
    size = queue.qsize()
    while not queue.empty():
        print ("Downloading [{}/{}]".format(index, size))
        image = queue.get()
        urllib.urlretrieve(image, os.path.basename(image))
        index += 1


def create_folder():
    folder_name = raw_input("What do you want to call your folder Name? ")
    # creates folder if it does not exist
    # I'm in linux so I'm ignoreing this bit....
    # but
    # path = FOLDER_PATH_FORMAT_STRING.format(username, folder_name)
    if os.path.exists(folder_name):
        os.chdir(folder_name)
    else:
        os.makedirs(folder_name)
        os.chdir(folder_name)


def main():
    processes = cpu_count() * 2
    queue = JoinableQueue()
    ans = 'y'

    while ans == 'y':

        get_links(queue)
        create_folder()

        for i in range(processes):
            p = Process(target=save_image, args=(queue,)).start()

        queue.join()
        queue.close()

        ans = raw_input("Do you have another link?(y/n)\n")


if __name__ == "__main__":
    main()
