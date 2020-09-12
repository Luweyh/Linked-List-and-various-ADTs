# Course: CS261 - Data Structures
# Student Name: Luwey Hon
# Assignment: Assignment 3 - Max_stack_sll
# Description: This program uses the LinkedList data strucutre
# created in sll.py. This program represent a Stack ADT for
# that single linked list.


from sll import *


class StackException(Exception):
    """
    Custom exception to be used by MaxStack Class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MaxStack:
    def __init__(self):
        """
        Init new MaxStack based on Singly Linked Lists
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.sll_val = LinkedList()
        self.sll_max = LinkedList()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "MAX STACK: " + str(self.sll_val.length()) + " elements. "
        out += str(self.sll_val)
        return out

    def push(self, value: object) -> None:
        """
        adds new element to top of stack
        """

        # setting up the max, adds the max in the front. if not the max then add back
        if self.sll_val.length() == 0:
            self.sll_max.add_front(value)
        elif value >= self.sll_max.get_front():
            self.sll_max.add_front(value)
        else:
            self.sll_max.add_back(value)

        self.sll_val.add_front(value)       # for the normal stack
        return

    def pop(self) -> object:
        """
        removes top element from the stack
        """

        # cant be empty
        if self.sll_val.length() == 0:
            raise StackException

        # save the top element and then remove it
        top_element = self.sll_val.get_front()
        self.sll_val.remove_front()
        self.sll_max.remove(top_element)        # remove max if it was pop

        return top_element


    def top(self) -> object:
        """
        returns top element without removing it
        """

        # cant be empty
        if self.sll_val.length() == 0:
            raise StackException

        return self.sll_val.get_front()

    def is_empty(self) -> bool:
        """
        see if the stack is empty
        """

        return self.sll_val.is_empty()

    def size(self) -> int:
        """
        returns the number of element in the stack
        """

        return self.sll_val.length()

    def get_max(self) -> object:
        """
        gets the maximum value in the stack
        """

        # stack cant be empty
        if self.sll_val.length() <= 0:
            raise StackException

        return self.sll_max.get_front()


# BASIC TESTING
if __name__ == "__main__":
    print('\n# push example 1')
    s = MaxStack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)

    # #
    # print('\n# pop example 1')
    # s = MaxStack()
    # try:
    #     print(s.pop())
    # except Exception as e:
    #     print("Exception:", type(e))
    # for value in [1, 2, 3, 4, 5]:
    #     s.push(value)
    # for i in range(6):
    #     try:
    #         print(s.pop())
    #     except Exception as e:
    #         print("Exception:", type(e))
    #

    # print('\n# top example 1')
    # s = MaxStack()
    # try:
    #     s.top()
    # except Exception as e:
    #     print("No elements in stack", type(e))
    # s.push(10)
    # s.push(20)
    # print(s)
    # print(s.top())
    # print(s.top())
    # print(s)

    # #
    # print('\n# is_empty example 1')
    # s = MaxStack()
    # print(s.is_empty())
    # s.push(10)
    # print(s.is_empty())
    # s.pop()
    # print(s.is_empty())

    #
    # print('\n# size example 1')
    # s = MaxStack()
    # print(s.size())
    # for value in [1, 2, 3, 4, 5]:
    #     s.push(value)
    # print(s.size())
    #
    #
    # print('\n# get_max example 1')
    # s = MaxStack()
    # for value in [1, -20, 15, 21, 21, 40, 50]:
    #     print(s, ' ', end='')
    #     try:
    #         print(s.get_max())
    #     except Exception as e:
    #         print(type(e))
    #     s.push(value)
    # while not s.is_empty():
    #     print(s.size(), end='')
    #     print(' Pop value:', s.pop(), ' get_max after: ', end='')
    #     try:
    #         print(s.get_max())
    #     except Exception as e:
    #         print(type(e))