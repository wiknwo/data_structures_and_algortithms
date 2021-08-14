class CircularDoublyLinkedList:
    """
    Class representing link-based CDLL in python
    """
    def __init__(self):
        """
        Initializes CDLL
        """
        self.__header = None
        self.__length = 0
        
    class Node:
        """
        Inner class representing node in DLL

        Attributes:
            data(Any): Data stored in node
            previous(Node): Pointer to node preceding this one
            next(Node): Pointer to node following this one
        
        Methods:
            get_data(): Returns the data stored in this node
            get_next(): Returns node following this one
            set_next(): Updates node following this one with new node
            get_previous(): Returns the node preceding this one
            set_previous(): Updates node preceding this one with new node
        """
        def __init__(self, data = None, previous = None, next = None):
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
            return self.__data
        
        def get_next(self):
            """
            Return node following this one

            Args:

            Return:
                Node following this one
                
            Raises: 
            """
            return self.__next
        
        def set_next(self, node):
            """
            Update the next node pointer of this node to node

            Args:
                node(Node): New node to update next pointer of this node

            Return:

            Raises:
            """
            self.__next = node
        
        def get_previous(self):
            """
            Return node before this one

            Args:

            Return:
                Node before this one

            Raises:
            """
            return self.__previous
        
        def set_previous(self, node):
            """
            Updates previous node of this node to new node

            Args:
                node: New node to become new previous of this node

            Return:

            Raises:
            """
            self.__previous = node