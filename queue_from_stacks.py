# Course: CS261 - Data Structures
# Student Name: Luwey Hon
# Assignment: Assignment 3 - queue_from_stacks
# Description: This program represent a Queue ADT.
# This uses the methods in MaxStack ADT to implement
# these specific Queue ADT.


from max_stack_sll import *


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Init new Queue based on two stacks
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.s1 = MaxStack()        # use as main storage
        self.s2 = MaxStack()        # use as temp storage

    def __str__(self) -> str:
        """
        Return content of queue in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "QUEUE: " + str(self.s1.size()) + " elements. "
        out += str(self.s1)
        return out

    def enqueue(self, value: object) -> None:
        """
        Adds a new value to the end of the queue
        """

        self.s1.push(value)
        return

    def dequeue(self) -> object:
        """
        removes and returns the value from the beginning
        """

        if self.s1.is_empty():
            raise QueueException

        length = self.s1.size()

        # looping to the end
        for num in range(length):

            # finds the beginning value then save it
            if num == length - 1:
                front_val = self.s1.pop()

            # pop the value and save it in temporary storage
            else:
                value = self.s1.pop()
                self.s2.push(value)

        # refill back main storage up to first node (non inclusive)
        for num in range(length-1):
            self.s1.push(self.s2.pop())

        return front_val

    def is_empty(self) -> bool:
        """
        return True if empty, else false
        """

        return self.s1.is_empty()

    def size(self) -> int:
        """
        returns the number of elements currently in queue
        """
        return self.s1.size()


# BASIC TESTING
if __name__ == "__main__":

    print('\n# enqueue example 1')
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)


    print('\n# dequeue example 1')
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for i in range(6):
        try:
            print(q.dequeue(), q)
        except Exception as e:
            print("No elements in queue", type(e))


    # print('\n# is_empty example 1')
    # q = Queue()
    # print(q.is_empty())
    # q.enqueue(10)
    # print(q.is_empty())
    # q.dequeue()
    # print(q.is_empty())
    #
    #
    # print('\n# size example 1')
    # q = Queue()
    # print(q.size())
    # for value in [1, 2, 3, 4, 5, 6]:
    #     q.enqueue(value)
    # print(q.size())
    #


