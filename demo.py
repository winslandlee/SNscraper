#!/usr/bin/env python
from multiprocessing import Process, JoinableQueue

# Messy, but acceptable config.
NUMBER_OF_CONSUMERS = 2

def put_in_numbers(queue):
    """
    The producer method, if you passed in another argument,
    like... a url this could run your scraping.
    """
    for i in range(100):
        queue.put(i)

    for i in range(NUMBER_OF_CONSUMERS):
        queue.put(None)

    queue.close()
    return


def get_number(queue):
    """
    The consumer method, if you put links in the queue
    these could do the downloading....
    """
    while True:
        number = queue.get(True)
        if number is None:
            ## End of the queue
            queue.task_done()
            return
        print(number * number)
        queue.task_done()


def main():
    '''
    The main function definition.
    '''

    queue = JoinableQueue()
    # Producer...
    # To fill the queue
    producer = Process(target=put_in_numbers, args=(queue,))
    producer.start()
    # Workers to work on the queue.
    workers = []
    for i in range(NUMBER_OF_CONSUMERS):
        p = Process(target=get_number, args=(queue,))
        p.start()
        workers.append(p)

    # and wait for everyone to finish
    # If the producer is done...
    producer.join()
    for worker in workers:
        # and the workers...
        worker.join()

    # And the queue no longer has any jobs....
    queue.join()

    print("Done")




if __name__ == '__main__':
    '''
    If this is the file being run...
    run main.
    '''
    main()
