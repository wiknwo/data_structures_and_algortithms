class CircularDoublyLinkedList:
    """
    Class representing link-based CDLL in python

    Attributes:
        header(Node): Head of the CDLL
        length(int): Length of the CDLL

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
        __iter__(): Returns an iterator for the linked list
        __next__(): Returns next node value in linked list
        __str__(): Retruns string representation of linked list
    """
    def __init__(self):
        """
        Initializes CDLL
        """
        self.__header = self.Node()
        self.__length = 0
        self.__current = self.__header # Pointer to current node for iterator
        self.__index = 0 # Index for iterator
        
    def size(self):
        """
        Returns size of CDLL
        """
        return self.__length

    def is_empty(self):
        """
        Returns boolean indicating if CDLL is empty
        """
        return self.__length == 0

    def first(self):
        """
        Returns value of head of CDLL
        """
        if self.is_empty():
            raise ValueError('CDLL is empty')
        return self.__header.get_data()

    def last(self):
        """
        Returns value of node preceding head of CDLL
        """
        if self.is_empty():
            raise ValueError('CDLL is empty')
        return self.__header.get_previous().get_data()
    
    def add_at_head(self, value):
        """
        Add new node with value at head of CDLL
        """
        new_node = self.Node(value)
        if self.is_empty():
            new_node.set_next(new_node)
            new_node.set_previous(new_node)
            self.__header = new_node
            self.__length += 1
        else:
            predecessor = self.__header.get_previous()
            successor = self.__header
            new_node.set_next(successor)
            new_node.set_previous(predecessor)
            successor.set_previous(new_node)
            predecessor.set_next(new_node)
            self.__header = new_node
            self.__length += 1
    
    def add_at_tail(self, value):
        """
        Add new node with value to end of CDLL
        """
        new_node = self.Node(value)
        if self.is_empty():
            new_node.set_next(new_node)
            new_node.set_previous(new_node)
            self.__header = new_node
            self.__length += 1
        else:
            self.__add_between(value, self.__header.get_previous(), self.__header)

    def __add_between(self, value, predecessor, successor):
        """
        Private helper method to add node between two nodes
        """
        new_node = self.Node(value, predecessor, successor)
        predecessor.set_next(new_node)
        successor.set_previous(new_node)
        self.__length += 1    

    def add_at_index(self, value, index):
        """
        Add node with value at specified index
        """
        if index > self.size() or index < 0:
            raise IndexError('Index out of bounds')
        
        if index == 0:
            return self.add_at_head(value)

        if index == self.size():
            return self.add_at_tail(value)
        
        i, current = 0, self.__header
        while i < self.__length:
            if i == index:
                predecessor = current.get_previous()
                successor = predecessor.get_next()
                self.__add_between(value, predecessor, successor)
                return 
            current = current.get_next()
            i += 1
            
    def remove_first(self):
        """
        Removes first node in CDLL amd retuns its value
        """
        if self.is_empty():
            raise ValueError('CDLL is empty')
        value = self.__header.get_data()
        predecessor = self.__header.get_previous()
        successor = self.__header.get_next()
        predecessor.set_next(successor)
        successor.set_previous(predecessor)
        self.__header = successor
        self.__length -= 1
        return value

    def remove_last(self):
        """
        Removes last node in CDLL and returns its value
        """
        if self.is_empty():
            raise ValueError('CDLL is empty')
        return self.__remove(self.__header.get_previous())
    
    def __remove(self, node):
        """
        Private helper method to remove node from DLL
        """
        predecessor = node.get_previous()
        successor = node.get_next()
        predecessor.set_next(successor)
        successor.set_previous(predecessor)
        self.__length -= 1
        return node.get_data()

    def delete_at_index(self, index):
        """
        Delete node with value at specified index
        """
        if index >= self.size() or index < 0:
            raise IndexError('Index out of bounds')
        
        if index == 0:
            return self.remove_first()

        if index == self.size() - 1:
            return self.remove_last()

        i, current = -1, None
        if index < self.size() // 2:
            i, current = 0, self.__header
            while current and i != index:
                current = current.get_next()
                i += 1
        else:
            i, current = self.size() - 1, self.__header.get_previous()
            while current and i != index:
                current = current.get_previous()
                i -= 1
        return self.__remove(current) 

    def delete(self, value):
        """
        Delete node with specified value from CDLL
        """
        # If CDLL is empty
        if self.is_empty():
            raise ValueError('CDLL is empty')
        # If CDLL contains only one node
        if self.__header.get_data() == value and self.__header.get_next() == self.__header:
            self.__header = self.Node()
            return
        # If head is to be deleted
        if self.__header.get_data() == value:
            return self.remove_first()
        # If the tail is to be deleted
        if self.__header.get_previous().get_data() == value:
            return self.remove_last()
        # If there is more than one node in CDLL
        current = self.__header
        # Traverse list till end reached or value found
        while current.get_next() != self.__header and current.get_data() != value:
            current = current.get_next()
        # If node to be deleted found
        if current.get_data() == value:
            return self.__remove(current)
        else:
            raise ValueError('Value not in CDLL')

    def get_by_index(self, index):
        """
        Return node's value at specified index
        """
        if index >= self.size() or index < 0:
            raise IndexError('Index out of bounds')

        if index == 0:
            return self.first()
        
        if index == self.size() - 1:
            return self.last()
        
        i, current = -1, None
        if index < self.size() // 2:
            i, current = 0, self.__header
            while current and i != index:
                current = current.get_next()
                i += 1
        else:
            i, current = self.size() - 1, self.__header.get_previous()
            while current and i != index:
                current = current.get_previous()
                i -= 1
        return current.get_data()

    def __iter__(self):
        """
        Returns iterator for CLL
        """
        # Remember, self is our UnorderedList.
        # In order to get to the first Node, we must do
        current = self.__header
        # and then, until we have reached the end:
        while True:
            yield current.get_data()
            # in order to get from one Node to the next one:
            current = current.get_next()
            if current == self.__header:
                break

    def __next__(self):  
        """
        Returns next node's value in CLL

        1. Define myiter = mycdll.__iter__()
        2. print(next(myiter))
        """
        if self.__current == self.__header and self.__index != 0:
            raise StopIteration
        value = self.__current.get_data()
        self.__current = self.__current.get_next()
        self.__index += 1
        return value

    def __str__(self):
        """
        Return string representation of CDLL
        """
        stringrep, current = '', self.__header
        while current.get_next() != self.__header:
            stringrep += '<- {} ->'.format(current.get_data())
            current = current.get_next()
        stringrep += '<- {} -> Back to head'.format(current.get_data())
        return stringrep

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

mycdll = CircularDoublyLinkedList()
mycdll.add_at_head('Eunice')
mycdll.add_at_head('Freda')
print('first: {}'.format(mycdll.first()))
mycdll.add_at_tail('Aretha')
print('last: {}'.format(mycdll.last()))
print(mycdll)
mycdll.add_at_index('Johnathon', 3)
print(mycdll)
print('first: {}'.format(mycdll.first()))
print('last: {}'.format(mycdll.last()))
mycdll.remove_first()
print(mycdll)
mycdll.add_at_head('Benjamin')
print(mycdll)
print(mycdll.size())
mycdll.remove_last()
print(mycdll)
print('last: {}'.format(mycdll.last()))
mycdll.delete_at_index(0)
print(mycdll)
mycdll.add_at_index('Benjamin', 2)
mycdll.add_at_tail('Winona')
mycdll.add_at_head('Barry')
print(mycdll)
print(mycdll.get_by_index(4))
for node in mycdll:
    print('Iterator: {}'.format(node))
myiter = mycdll.__iter__()
for i in range(mycdll.size()):
    print('Next: {}'.format(next(myiter)))
print(mycdll)
mycdll.delete('Eunice')
print(mycdll)
mycdll.add_at_index('Oliver', 4)
print(mycdll)
