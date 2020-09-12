# Course: CS261 - Data Structures
# Student Name: Luwey Hon
# Assignment: Assignment 3 - CDLL
# Description: This program represent a circular
# double linked list which means that each node is connected
# to each other both way. It implements several ADT that is
# specific to the CDLL.


class CDLLException(Exception):
    """
    Custom exception class to be used by Circular Doubly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DLNode:
    """
    Doubly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        self.next = None
        self.prev = None
        self.value = value


class CircularList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with sentinel
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.sentinel = DLNode(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

        # populate CDLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'CDLL ['
        if self.sentinel.next != self.sentinel:
            cur = self.sentinel.next.next
            out = out + str(self.sentinel.next.value)
            while cur != self.sentinel:
                out = out + ' <-> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def add_front(self, value: object) -> None:
        """
        Adds node to the beginning
        """

        node = DLNode(value)  # create node

        # double linking the nodes in both directions
        node.prev = self.sentinel
        node.next = self.sentinel.next
        self.sentinel.next = node
        node.next.prev = node
        return

    def add_back(self, value: object) -> None:
        """
        add node to the back of the list
        """

        prev = self.sentinel.prev
        curr = self.sentinel

        while curr.next != self.sentinel:
            prev = curr
            curr = curr.next

        node = DLNode(value)

        # double linking the nodes at the end of linked list
        curr.next = node
        node.prev = curr
        node.next = self.sentinel
        self.sentinel.prev = node

        return

    def insert_at_index(self, index: int, value: object) -> None:
        """
        add a new node to a specified position
        """

        # can't be negative index
        if index < 0:
            raise CDLLException

        prev = self.sentinel.prev
        curr = self.sentinel

        for pos in range(index + 1):

            prev = curr
            curr = curr.next

            # ouf of range when current become first node and it's not the first iteration
            if curr == self.sentinel.next and pos != 0:
                raise CDLLException

        # create and link the nodes
        node = DLNode(value)
        node.next = curr
        node.prev = prev
        prev.next = node
        curr.prev = node

        return

    def remove_front(self) -> None:
        """
        removes the front node
        """

        prev = self.sentinel
        curr = self.sentinel.next

        # can't be empty
        if curr == self.sentinel:
            raise CDLLException

        # removing the front node and linking them
        prev.next = curr.next
        curr.next.prev = self.sentinel

        return

    def remove_back(self) -> None:
        """
        removes the back node
        """
        previous = self.sentinel
        curr = self.sentinel.prev

        # can't be empty
        if curr == self.sentinel:
            raise CDLLException

        # removing the back and linking
        previous.prev = curr.prev
        curr.prev.next = previous
        return

    def remove_at_index(self, index: int) -> None:
        """
        removes a node a certain in dex
        """

        if index < 0:
            raise CDLLException

        prev = self.sentinel
        curr = self.sentinel.next

        # can't remove an empty list
        if curr == self.sentinel:
            raise CDLLException

        for num in range(index):
            # ouf of range
            if curr.next == self.sentinel:
                raise CDLLException

            prev = curr
            curr = curr.next

        prev.next = curr.next
        curr.next.prev = prev
        return

    def get_front(self) -> object:
        """
        returns the front node without removing it
        """

        curr = self.sentinel.next

        # when the list is empty
        if curr == self.sentinel:
            raise CDLLException

        return curr.value

    def get_back(self) -> object:
        """
        returns the back node without removing it
        """

        curr = self.sentinel.prev

        # when the list is empty
        if curr == self.sentinel:
            raise CDLLException

        return curr.value

    def remove(self, value: object) -> bool:
        """
        removes the first node with the given value
        """

        prev = None
        curr = self.sentinel

        while curr.next != self.sentinel:
            prev = curr
            curr = curr.next

            # when the current value is found, remove it and update links
            if curr.value == value:
                prev.next = curr.next
                curr.next.prev = prev
                return True

        return False

    def count(self, value: object) -> int:
        """
        counts the number of elements that match the value
        """

        curr = self.sentinel
        count = 0

        # counts every index till reach end of list
        while curr.next != self.sentinel:
            if curr.next.value == value:
                count += 1
            curr = curr.next            # update the current pos

        return count

    def slice(self, start_index: int, size: int) -> object:
        """
        returns a new list that is sliced depending on the
        starting index and size
        """

        if start_index < 0:
            raise CDLLException

        prev = None
        curr = self.sentinel

        # iterating up to index and updating the nodes
        for num in range(start_index + 1):
            if curr.next == self.sentinel:
                raise CDLLException
            prev = curr
            curr = curr.next

        new_list = CircularList()
        count = 0

        # appends the current node value to the list
        for num in range(size):
            if curr == self.sentinel:
                raise CDLLException
            new_list.insert_at_index(count, curr.value)     # inserts current node value here
            curr = curr.next
            count += 1

        return new_list

    def is_sorted(self) -> int:
        """
        returns 1 if strictly ascending, return 2 is descending,
        returns 0 if neither
        """

        prev = self.sentinel
        curr = self.sentinel.next

        # if it is empty or has one node, then its ascending
        if curr == self.sentinel or curr.next == self.sentinel:
            return 1

        is_ascending = 0
        is_descending = 0
        is_neither = 0

        while curr.next != self.sentinel:
            prev = curr
            curr = curr.next

            # descending condition
            if prev.value > curr.value:
                is_descending += 1

            # ascending condition
            elif prev.value < curr.value:
                is_ascending += 1

            # when they're equal, they're neither
            elif prev.value == curr.value:
                is_neither += 1

        # can't be ascending or descending
        if is_neither > 0:
            return 0

        # condition when all elements are ascending
        if is_ascending > 0 and is_descending == 0:
            return 1

        # condition when all elements or descending
        if is_descending > 0 and is_ascending == 0:
            return 2

        return 0

    def swap_pairs(self, index1: int, index2: int) -> None:
        """
        Swaps the pairs depending on index
        """

        if index1 < 0 or index2 < 0:
            raise CDLLException

        prev_1 = self.sentinel
        curr_1 = self.sentinel.next

        if curr_1 == self.sentinel:
            raise CDLLException

        for num in range(index1):
            if curr_1.next == self.sentinel:
                raise CDLLException
            prev_1 = curr_1
            curr_1 = curr_1.next


        prev_2 = self.sentinel
        curr_2 = self.sentinel.next

        for num in range(index2):
            if curr_2.next == self.sentinel:
                raise CDLLException
            prev_2 = curr_2
            curr_2 = curr_2.next

        # swapping the pairs once the position is found
        curr_1.prev.next = curr_2
        curr_1.next.prev = curr_2
        curr_2.prev.next = curr_1
        curr_2.next.prev = curr_1
        curr_2.next, curr_1.next = curr_1.next, curr_2.next
        curr_2.prev, curr_1.prev = curr_1.prev, curr_2.prev

        return

    def reverse(self) -> None:
        """
        reverses the nodes in the list
        """
        back_node = None
        front_node = self.sentinel

        # iterating through whole list and reversing
        for num in range(self.length() + 1):
            back_node = front_node.prev
            front_node.prev = front_node.next
            front_node.next = back_node
            front_node = front_node.prev

        return

    def sort(self) -> None:
        """
        Sorts it in ascending order
        """

        length = self.length()

        if self.length() >= 2:                   # can only sort when there's at least two elements

            # bubble sort
            for num in range(length*2):
                curr_1 = self.sentinel              # reset nodes to beginning
                curr_2 = self.sentinel.next

                for pos in range(length-1):

                    curr_1 = curr_2                 # updating the nodes
                    curr_2 = curr_2.next

                    # swap elements when left node > right node
                    if curr_1.value > curr_2.value:
                        self.insert_at_index(pos+1, 'flag')         # flag for buffer to swap non adjacent
                        self.swap_pairs(pos, pos + 2)               # swap the nodes
                        self.remove('flag')                         # remove buffer

        return

    def length(self) -> int:
        """
        returns the number of nodes
        """

        curr = self.sentinel
        count = 0

        # traverse through whole linked list and counts
        while curr.next != self.sentinel:
            count += 1
            curr = curr.next

        return count

    def is_empty(self) -> bool:
        """
        returns true if the the list is empty
        """

        # it's empty when the length is more than 0
        if self.length() > 0:
            return False

        return True


if __name__ == '__main__':
    #     print('\n# add_front example 1')
    #     list = CircularList()
    #     print(list)
    #     list.add_front('A')
    #     list.add_front('B')
    #     list.add_front('C')
    #     print(list)
    # #
    # #
    #     print('\n# add_back example 1')
    #     list = CircularList()
    #     print(list)
    #     list.add_back('C')
    #     list.add_back('B')
    #     list.add_back('A')
    #     print(list)
    # #
    #
    # print('\n# insert_at_index example 1')
    # list = CircularList()
    # test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    # for index, value in test_cases:
    #     print('Insert of', value, 'at', index, ': ', end='')
    #     try:
    #         list.insert_at_index(index, value)
    #         print(list)
    #     except Exception as e:
    #         print(type(e))

#
    # print('\n# remove_front example 1')
    # list = CircularList([1, 2])
    # print(list)
    # for i in range(3):
    #     try:
    #         list.remove_front()
    #         print('Successful removal', list)
    #     except Exception as e:
    #         print(type(e))

#
    # print('\n# remove_back example 1')
    # list = CircularList()
    # try:
    #     list.remove_back()
    # except Exception as e:
    #     print(type(e))
    # list.add_front('Z')
    # list.remove_back()
    # print(list)
    # list.add_front('Y')
    # list.add_back('Z')
    # list.add_front('X')
    # print(list)
    # list.remove_back()
    # print(list)
#

    # print('\n# get_front example 1')
    # list = CircularList(['A', 'B'])
    # print(list.get_front())
    # print(list.get_front())
    # list.remove_front()
    # print(list.get_front())
    # list.remove_back()
    # try:
    #     print(list.get_front())
    # except Exception as e:
    #     print(type(e))

#
    # print('\n# get_back example 1')
    # list = CircularList([1, 2, 3])
    # list.add_back(4)
    # print(list.get_back())
    # list.remove_back()
    # print(list)
    # print(list.get_back())
#
#
    # print('\n# remove example 1')
    # list = CircularList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    # print(list)
    # for value in [7, 3, 3, 3, 3]:
    #     print(list.remove(value), list.length(), list)


    # print('\n# count example 1')
    # list = CircularList([1, 2, 3, 1, 2, 2])
    # print(list, list.count(1), list.count(2), list.count(3), list.count(4))

#
    # print('\n# slice example 1')
    # list = CircularList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    # ll_slice = list.slice(1, 3)
    # print(list, ll_slice, sep="\n")
    # ll_slice.remove_at_index(0)
    # print(list, ll_slice, sep="\n")
    #
    #
    # print('\n# slice example 2')
    # list = CircularList([10, 11, 12, 13, 14, 15, 16])
    # print("SOURCE:", list)
    # slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    # for index, size in slices:
    #     print("Slice", index, "/", size, end="")
    #     try:
    #         print(" --- OK: ", list.slice(index, size))
    #     except:
    #         print(" --- exception occurred.")
#
#
    # print('\n# is_sorted example 1')
    # test_cases = (
    #     [-100, -8, 0, 2, 3, 10, 20, 100],
    #     ['A', 'B', 'Z', 'a', 'z'],
    #     ['Z', 'T', 'K', 'A', '1'],
    #     [1, 3, -10, 20, -30, 0],
    #     [-10, 0, 0, 10, 20, 30],
    #     [100, 90, 0, -90, -200]
    # )
    # for case in test_cases:
    #     list = CircularList(case)
    #     print('Result:', list.is_sorted(), list)

#
#     print('\n# is_empty example 1')
#     list = CircularList()
#     print(list.is_empty(), list)
#     list.add_back(100)
#     print(list.is_empty(), list)
#     list.remove_at_index(0)
#     print(list.is_empty(), list)
#
#
#     print('\n# length example 1')
#     list = CircularList()
#     print(list.length())
#     for i in range(800):
#         list.add_front(i)
#     print(list.length())
#     for i in range(799, 300, -1):
#         list.remove_at_index(i)
#     print(list.length())
# #
#     print('\n# swap_pairs example 1')
#     list = CircularList([0, 1, 2, 3, 4, 5, 6])
#     test_cases = ((0, 6), (0, 7), (-1, 6), (1, 5), (4, 2), (3, 3))
#
#     for i, j in test_cases:
#         print('Swap nodes ', i, j, ' ', end='')
#         try:
#             list.swap_pairs(i, j)
#             print(list)
#         except Exception as e:
#             print(type(e))

#
#     print('\n# reverse example 1')
#     test_cases = (
#         [1, 2, 3, 3, 4, 5],
#         [1, 2, 3, 4, 5],
#         ['A', 'B', 'C', 'D']
#     )
#     for case in test_cases:
#         list = CircularList(case)
#         list.reverse()
#         print(list)
# #
#
    # print('\n# reverse example 2')
    # list = CircularList()
    # print(list)
    # list.reverse()
    # print(list)
    # list.add_back(2)
    # list.add_back(3)
    # list.add_front(1)
    # list.reverse()
    # print(list)

#
    print('\n# sort example 1')
    test_cases = (
        [1, 10, 2, 20, 3, 30, 4, 40, 5],
        ['zebra2', 'apple', 'tomato', 'apple', 'zebra1'],
        [(1, 1), (20, 1), (1, 20), (2, 20)]
    )
    for case in test_cases:
        list = CircularList(case)
        print(list)
        list.sort()
        print(list)

    # list = CircularList([1,10,2,20])
    # list.sort()
    # print(list)
