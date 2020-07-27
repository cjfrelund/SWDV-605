# week_04.py

from DLB import LinkedDeque
import time

# A STACK example that demenstrates a first in last out linear data structure.


def stack_example():
    myStackedList = LinkedDeque()

    time.sleep(1)
    myStackedList.insert_last('One')
    print(myStackedList.last())

    time.sleep(1)
    myStackedList.insert_last('Two')
    print(myStackedList.last())

    time.sleep(1)
    myStackedList.insert_last('Three')
    print(myStackedList.last())

    print("\nNow time to remove items from the stack (FILO).\n")
    time.sleep(3)
    print(myStackedList.last())

    time.sleep(1)
    myStackedList.delete_last()
    print(myStackedList.last())

    time.sleep(1)
    myStackedList.delete_last()
    print(myStackedList.last())


def queue_example():
    myQueuedList = LinkedDeque()

    time.sleep(1)
    myQueuedList.insert_first('Apple')
    print(myQueuedList.first())

    time.sleep(1)
    myQueuedList.insert_first('Pear')
    print(myQueuedList.first())

    time.sleep(1)
    myQueuedList.insert_first('Mango')
    print(myQueuedList.first())

    time.sleep(1)
    print("\nNow time to remove items from the Queue (FIFO)\n")
    time.sleep(3)
    print(myQueuedList.last())

    time.sleep(1)
    myQueuedList.delete_last()
    print(myQueuedList.last())

    time.sleep(1)
    myQueuedList.delete_last()
    print(myQueuedList.last())


def deque_example():
    myQueuedList = LinkedDeque()

    time.sleep(1)
    myQueuedList.insert_first('First')
    print(myQueuedList.first())

    time.sleep(1)
    myQueuedList.insert_last('Last')
    print(myQueuedList.last())

    time.sleep(1)
    myQueuedList.insert_first('NewFirst')
    print(myQueuedList.first())

    time.sleep(1)
    print("\nFirst was first in, and then Last was added after First.  \nThen NewFirst was added ahead of First, making it the NewFirst Node.  \nNow removing each Node from the first position, I should see NewFirst removed first.\n")
    time.sleep(3)
    print(myQueuedList.first())

    time.sleep(1)
    myQueuedList.delete_first()
    print(myQueuedList.first())

    time.sleep(1)
    myQueuedList.delete_first()
    print(myQueuedList.first())


def main():
    print("\nThe following code example showcases the use of a doubly linked list \nand node class for use as a STACK implementation, a QUEUE \nimplementation, and DEQUE implementation.\n")
    # Example of a STACK implementation.
    print("\nLet's start with a STACK.\n")
    time.sleep(3)
    stack_example()
    time.sleep(3)

    # Example of a QUEUE implementation.
    print("\nNow for a QUEUE.\n")
    time.sleep(3)
    queue_example()

    # Example of a DEQUE implementation.
    print("\nNow for a DEQUE.\n")
    time.sleep(3)
    deque_example()


if __name__ == "__main__":
    main()
