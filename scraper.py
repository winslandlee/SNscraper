import requests
import os
import shutil
from urllib.parse import urlparse
from multiprocessing import cpu_count, JoinableQueue, Process
from bs4 import BeautifulSoup
# Python2/3 Compatability.
try:
    input = raw_input
except NameError:
    pass

FOLDER_PATH_FORMAT_STRING = "C:\\Users\\{}\\Pictures\\StanceNation\\{}"


def get_image_name(url):
    parsed = urlparse(url)
    return os.path.split(parsed.path)[1]


def get_links(queue):
    url = input("What is the StanceNation link?\n")
    if 'http://' not in url:
        url = 'http://' + url

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    for image in soup.findAll('meta', {"property": 'og:image'}):
        if '1140' or '1500' in image['content']:
            queue.put(image['content'])


def save_image(queue):
    # index = 1
    # Individual index for each process? Not that useful.
    # size = queue.qsize()
    image = queue.get()  # Blocking
    while image is not None:
        # print ("Downloading [{}/{}]".format(index, size))
        filename = get_image_name(image)
        response = requests.get(image, stream=True)
        with open(filename, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        print("{} Done.".format(filename))
        print("{} images left".format(queue.qsize()))
        del response
        queue.task_done() ## Need to call this to join it later
        image = queue.get()
    queue.task_done() ## Need to call this to join it later


def create_folder():
    folder_name = input("What do you want to call your folder?")
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
    get_links(queue)
    create_folder()

    for i in range(processes):
        # .start() - Not sure what that actually returns....
        p = Process(target=save_image, args=(queue,))
        p.start()

    for i in range(processes):
        queue.put(None) ## Tell the processes to end

    queue.join()
    queue.close()


if __name__ == "__main__":
    main()
