#!/usr/bin/env python
from multiprocessing import Process, JoinableQueue

# Messy, but acceptable config.
NUMBER_OF_CONSUMERS = 2

def put_in_numbers(queue):
    for i in range(100):
        queue.put(i)

    for i in range(NUMBER_OF_CONSUMERS):
        queue.put(None)

    queue.close()
    return


def get_number(queue):
    ## Blocking... going to sit there for a while.
    print("Process")
    while True:
        number = queue.get(True)
        if number is None:
            ## End of the queue
            queue.task_done()
            return
        print(number * number)
        queue.task_done()


def main():

    queue = JoinableQueue()
    # Produucer...
    # Fill it fuill of crap
    producer = Process(target=put_in_numbers, args=(queue,))
    producer.start()
    # Workers
    workers = []
    for i in range(NUMBER_OF_CONSUMERS):
        p = Process(target=get_number, args=(queue,))
        p.start()
        workers.append(p)

    # and wait for everyone to finish

    producer.join()
    for worker in workers:
        worker.join()

    # queue.join()
    queue.join()




if __name__ == '__main__':
    main()
