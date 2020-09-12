# Course: CS261 - Data Structures
# Student Name: Luwey Hon
# Assignment: Assignment 3 - sll
# Description: This program represent a a single linked
# list. It creates the list and implements several ADT
# specific to this list


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class SLNode:
    """
    Singly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with front and back sentinels
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.head = SLNode(None)
        self.tail = SLNode(None)
        self.head.next = self.tail

        # populate SLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        if self.head.next != self.tail:
            cur = self.head.next.next
            out = out + str(self.head.next.value)
            while cur != self.tail:
                out = out + ' -> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def add_front(self, value: object) -> None:
        """
        Adds a node to the beginning of the linked list
        """

        node = SLNode(value)
        node.next = self.head.next      # next node becomes next head
        self.head.next = node           # next head becomes new node
        return

    def add_back(self, value: object) -> None:
        """
        Adds a node to the back of the linked list
        """
        node = SLNode(value)

        current = self.head.next
        previous = self.head

        # previous nodes becomes the current, and current node becomes next
        while current != self.tail:
            previous = current
            current = current.next

        # adding the back node and updating the tail
        previous.next = node
        node.next = self.tail
        return

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Insert a node at a certain index
        """

        some_node = self.head

        # valid indexes are >= 0
        if index < 0:
            raise SLLException

        # iterating until reach to index
        for num in range(index):
            some_node = some_node.next
            if some_node == self.tail:
                raise SLLException

        # node can't be none
        if some_node == None:
            raise SLLException

        # create the new node and insert at the index
        new_node = SLNode(value)
        new_node.next = some_node.next
        some_node.next = new_node

        return

    def remove_front(self) -> None:
        """
        removes the front node
        """

        # can't remove when there is no nodes
        if self.head.next == self.tail:
            raise SLLException()

        self.head.next = self.head.next.next

        return

    def remove_back(self) -> None:
        """
        removes the back node
        """

        previous = None
        current = self.head

        # when there's no node to remove
        if current.next == self.tail:
            raise SLLException

        # get to the last element
        while current.next != self.tail:
            previous = current
            current = current.next

        # removes last node and replace it with the tail
        previous.next = self.tail

        return

    def remove_at_index(self, index: int) -> None:
        """
        removes the node at a certain index
        """

        prev = self.head
        current = self.head.next

        # index cant be negative or empty
        if index < 0 or current == self.tail:
            raise SLLException

        # iteration to find the node at index
        for num in range(index):

            # in case it removes out of range
            if current.next == self.tail:
                raise SLLException

            prev = current
            current = current.next

        # removing the index
        prev.next = current.next

        return

    def get_front(self) -> object:
        """
        gets the front node
        """

        if self.head.next == self.tail:
            raise SLLException

        return self.head.next.value

    def get_back(self) -> object:
        """
        gets the back node
        """
        prev = self.head
        current = self.head.next

        # can't be empty
        if current == self.tail:
            raise SLLException

        # iterating to last node
        while current.next != self.tail:
            prev = current
            current = current.next

        return current.value

    def remove(self, value: object) -> bool:
        """
        removes a node and returns true if found
        else returns false
        """
        prev = self.head
        cur = self.head.next

        count = 0
        while cur.next != self.tail:
            if cur.value == value:
                self.remove_at_index(count)
                return True
            prev = cur
            cur = cur.next
            count += 1

        return False

    def count(self, value: object) -> int:
        """
        counts the number of elements that match
        the provided value
        """

        prev = self.head
        curr = self.head.next
        count = 0

        while curr != self.tail:
            if curr.value == value:
                count += 1
            prev = curr
            curr = curr.next

        return count

    def slice(self, start_index: int, size: int) -> object:
        """
        Slices the linked list by a starting index and stops
        depending on the size
        """

        prev = self.head
        curr = self.head.next

        # can't slice no nodes
        if curr == self.tail:
            raise SLLException

        # starting index cant be negative
        if start_index < 0:
            raise SLLException

        # finding the right index
        for num in range(start_index):
            if curr.next == self.tail:      # check out of range
                raise SLLException
            prev = curr
            curr = curr.next

        new_list = LinkedList()
        count = 0

        # appending the new node into the new list
        for num in range(size):
            if curr == self.tail:           # check ouf of range
                raise SLLException
            prev = curr
            curr = curr.next
            new_list.insert_at_index(count, prev.value)     # inserts the node value to the new list
            count += 1

        return new_list

    def is_sorted(self) -> int:
        """
        Checks to see if it is ascending, descending or neither
        """

        prev = self.head
        curr = self.head.next

        is_ascending = 0
        is_descending = 0
        neither = 0

        while curr.next != self.tail:
            prev = curr
            curr = curr.next

            # it is ascending when prev < current
            if prev.value < curr.value:
                is_ascending += 1

            # it is descending when prev > current
            elif prev.value > curr.value:
                is_descending += 1

            # it is neither when they are the same value
            elif prev.value == curr.value:
                neither += 1

        # see if it is neither
        if neither > 0:
            return 0

        # when there's no node, its ascending. this also include the one node condition
        if is_ascending == 0 and is_descending == 0:
            return 1

        # see if it is ascending
        if is_ascending > 0 and is_descending == 0:
            return 1

        # see if it is descending
        if is_descending > 0 and is_ascending == 0:
            return 2

        # all option fails so its neither
        return 0

    def length(self) -> int:
        """
        returns the number of nodes in the list
        """
        prev = None
        curr = self.head
        count = 0

        # counts the node every iteration until reach end of list
        while curr.next != self.tail:
            prev = curr
            curr = curr.next
            count += 1

        return count

    def is_empty(self) -> bool:
        """
        see if the linked list is empty
        """

        # it is not empty when the length is > 0
        if self.length() > 0:
            return False

        return True


if __name__ == '__main__':
    # print('\n# add_front example 1')
    # list = LinkedList()
    # print(list)
    # list.add_front('A')
    # list.add_front('B')
    # list.add_front('C')
    # print(list)
    #
    #
    # print('\n# add_back example 1')
    # list = LinkedList()
    # print(list)
    # list.add_back('C')
    # list.add_back('B')
    # list.add_back('A')
    # print(list)


    # print('\n# insert_at_index example 1')
    # list = LinkedList()
    # test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    # for index, value in test_cases:
    #     print('Insert of', value, 'at', index, ': ', end='')
    #     try:
    #         list.insert_at_index(index, value)
    #         print(list)
    #     except Exception as e:
    #         print(type(e))

    # print('\n# remove_front example 1')
    # list = LinkedList([1, 2])
    # print(list)
    # for i in range(3):
    #     try:
    #         list.remove_front()
    #         print('Successful removal', list)
    #     except Exception as e:
    #         print(type(e))
    #
    #
    # print('\n# remove_back example 1')
    # list = LinkedList()
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
    # print('\n# remove_at_index example 1')
    # list = LinkedList([1, 2, 3, 4, 5, 6])
    # print(list)
    # for index in [0, 0, 0, 2, 2, -2]:
    #     print('Removed at index:', index, ': ', end='')
    #     try:
    #         list.remove_at_index(index)
    #         print(list)
    #     except Exception as e:
    #         print(type(e))
    # print(list)


    # print('\n# get_front example 1')
    # list = LinkedList(['A', 'B'])
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
    # list = LinkedList([1, 2, 3])
    # list.add_back(4)
    # print(list.get_back())
    # list.remove_back()
    # print(list)
    # print(list.get_back())
    # #
    #
    # print('\n# remove example 1')
    # list = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    # print(list)
    # for value in [7, 3, 3, 3, 3]:
    #     print(list.remove(value), list.length(), list)

    #
    # print('\n# count example 1')
    # list = LinkedList([1, 2, 3, 1, 2, 2])
    # print(list, list.count(1), list.count(2), list.count(3), list.count(4))


    print('\n# slice example 1')
    list = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = list.slice(1, 3)
    print(list, ll_slice, sep="\n")
    ll_slice.remove_at_index(0)
    print(list, ll_slice, sep="\n")

    #
    # print('\n# slice example 2')
    # list = LinkedList([10, 11, 12, 13, 14, 15, 16])
    # print("SOURCE:", list)
    # slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    # for index, size in slices:
    #     print("Slice", index, "/", size, end="")
    #     try:
    #         print(" --- OK: ", list.slice(index, size))
    #     except:
    #         print(" --- exception occurred.")

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
    #     list = LinkedList(case)
    #     print('Result:', list.is_sorted(), list)
    #
    #
    # print('\n# is_empty example 1')
    # list = LinkedList()
    # print(list.is_empty(), list)
    # list.add_back(100)
    # print(list.is_empty(), list)
    # list.remove_at_index(0)
    # print(list.is_empty(), list)


    # print('\n# length example 1')
    # list = LinkedList()
    # print(list.length())
    # for i in range(800):
    #     list.add_front(i)
    # print(list.length())
    # for i in range(799, 300, -1):
    #     list.remove_at_index(i)
    # print(list.length())
