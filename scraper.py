import requests, Queue, os, getpass, urllib
from threading import Thread
from bs4 import BeautifulSoup

try:
    input = raw_input
except NameError:
    pass


def save_image(queue):
    index = 1
    size = queue.qsize()
    while not queue.empty():
        print ('Downloading [{}/{}]'.format(index, size))
        image = queue.get()
        urllib.urlretrieve(image, os.path.basename(image))
        index += 1


def create_folder():
    folder_name = input('What do you want to call your folder Name? ')
    # Creates folder if it does not exist
    folder_string = 'C:\\Users\\{}\\Pictures\\StanceNation\\{}'.format(
        getpass.getuser(), folder_name)

    if os.path.exists(folder_string):
        os.chdir(folder_string)
    else:
        os.makedirs(folder_string)
        os.chdir(folder_string)


def main():
    ans = 'y'
    while ans == 'y':
        url = input('What is the StanceNation link?\n')
        if 'http://' not in url:
            url = 'http://' + url

        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        queue = Queue.LifoQueue()
        create_folder()
        for image in soup.findAll('meta', {'property': 'og:image'}):
            if '1140' or '1500' in image['content']:
                queue.put(image['content'])

        for i in range(10):
            thread_num_1 = Thread(save_image(queue))
            thread_num_2 = Thread(save_image(queue))
            thread_num_1.start()
            thread_num_2.start()

        ans = raw_input('Do you have another link?(y/n)\n')

if __name__ == '__main__':
    main()
