class DoublyLinkedList:
    """
    Class representing linked list data type in python

    Attributes:
        Node(Inner Class): Inner class representing node in linked list.
        head(Node): Head of the linked list
        tail(Node): Tail of the linked list
        current_node(Node): Pointer to the current node for linked list iterator
        length(int): Size of the linked list

    Methods:
        size(): Returns size of linked list
        is_empty(): Returns boolean indicating if linked list is empty
        first(): Returns first node value in linked list
        last(): Returns last node value in linked list
        get_by_index(index): Retuns value of node at specified index
        add_at_head(value): Adds new node to head of linked list and gives it value
        add_at_tail(value): Adds new node to tail of linked list and gives it value
        add_at_index(value, index): Adds new node with value at specified index in linked list
        delete_at_index(index): Deletes node at specified index
        delete(value): Deletes node with given value from linked list
        removeFirst(): Deletes first node from linked list
        removeLast(): Deletes last node from linked list
        contains(value): Returns boolean indicating if value is in linked list
        floyds_cycle_finding_algorithm(): Returns boolean indicating if there is a cycle in linked list
        sort(): Sorts linked list in ascending ordere
        get_midpoint(): Returns middle value of linked list
        __iter__(): Returns an iterator for the linked list
        __next__(): Returns next node value in linked list
        __str__(): Retruns string representation of linked list
    """
    class Node:
        """
        Inner class representing node in DLL

        Attributes:

        """
        def __init__(self, data = None, next = None, previous = None):
            """
            Initialize node with data and pointers to next and previous nodes

            Args:
                data: Data to be stored in node
                next(Node): Pointer to node following this one
                previous(Node): Pointer to node before this one

            Return:

            Raises:
            """
            self.__data = data
            self.__previous = previous
            self.__next = next

        def get_data(self):
            """
            Return data stored in node

            Args:

            Return:
                Data stored in node

            Raises
            """