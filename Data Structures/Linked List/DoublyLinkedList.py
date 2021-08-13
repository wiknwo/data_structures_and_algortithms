class DoublyLinkedList:
    """
    Class representing linked list data type in python

    Attributes:
        Node(Inner Class): Inner class representing node in linked list.
        header(Node): Head of the linked list
        trailer(Node): Tail of the linked list
        current(Node): Pointer to current node for iterator
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
        __iter__(): Returns an iterator for the linked list
        __next__(): Returns next node value in linked list
        __str__(): Retruns string representation of linked list
    """
    def __init__(self):
        """
        Initializes doubly linked list

        Args:

        Return:

        Raises:
        """
        self.__header = self.Node(None, None, None) # Create header
        self.__trailer = self.Node(None, self.__header, None) # Trailer is preceded by header
        self.__header.set_next(self.__trailer) # Header is followed by trailer
        self.__current = self.__header.get_next() # Pointer to current node in DLL for iterator
        self.__length = 0 # Number of nodes in linked list

    def size(self):
        """
        Return size of DLL

        Args:

        Return:
            Number of nodes in DLL

        Raises:
        """
        return self.__length
    
    def is_empty(self):
        """
        Return boolean indicating if DLL is empty

        Args:

        Return:
            Boolean indicating if DLL is empty

        Raises:
        """
        return self.__length == 0
    
    def first(self):
        """
        Return first node's value in DLL

        Args:

        Return:
            First node's value in DLL

        Raises:
            ValueError: Empty DLL
        """
        if self.is_empty():
            raise ValueError('Empty DLL')
        return self.__header.get_next().get_data()
    
    def last(self):
        """
        Return last node's value in DLL

        Args:

        Return:
            Value of last node in DLL

        Raises:
            ValueError: Empty DLL
        """
        if self.is_empty():
            raise ValueError('Empty DLL')
        return self.__trailer.get_previous().get_data()

    def add_at_head(self, value):
        """
        Add new node to head of DLL

        Args:
            value: Value to be associated with new node

        Return:

        Raises:
        """
        if self.is_empty():
            self.__add_between(value, self.__header, self.__trailer)
        else:
            self.__add_between(value, self.__header, self.__header.get_next())
    
    def __add_between(self, value, predecessor, successor):
        """
        Private helper method to add node between two nodes

        Args:
            predecessor(Node): Node preceding new node
            successor(Node): Node following new node

        Return

        Raises:
        """
        new_node = self.Node(value, predecessor, successor)
        predecessor.set_next(new_node)
        successor.set_previous(new_node)
        self.__length += 1

    def add_at_tail(self, value):
        """
        Add new node with value to end of DLL

        Args:
            value: Value to associate with new node

        Return:

        Raises:
        """
        if self.is_empty():
            self.__add_between(value, self.__header, self.__trailer)
        else:
            self.__add_between(value, self.__trailer.get_previous(), self.__trailer)

    def add_at_index(self, value, index):
        """
        Adds new node at specified index in DLL

        Args:
            value: Value to associate with new node at specified index
            index(int): Specified index at which to add new node

        Return:

        Raises:
            ValueError: Index out of bounds
        """
        if index > self.size() or index < 0:
            raise ValueError('Index out of bounds')
        
        if index == 0:
            return self.add_at_head(value)
            
        if index == self.size():
            return self.add_at_tail(value)
        
        i, current = 0, self.__header.get_next()
        while current and i < self.__length:
            if i == index:
                predecessor = current.get_previous()
                successor = predecessor.get_next()
                self.__add_between(value, predecessor, successor)
                return None
            current = current.get_next()
            i += 1
    
    def get_by_index(self, index):
        """
        Return value of node at specified index

        Args:
            index(int): Index of node to return

        Return:
            Value of node at specified index

        Raises:
            ValueError: Index out of bounds
        """
        if index >= self.size() or index < 0:
            raise ValueError('Index out of bounds')

        if index == 0:
            return self.first()
        
        if index == self.size() - 1:
            return self.last()

        i, current = -1, None
        if index < self.size() // 2:
            i, current = 0, self.__header.get_next()
            while current and i != index:
                current = current.get_next()
                i += 1
        else:
            i, current = self.size() - 1, self.__trailer.get_previous()
            while current and i != index:
                current = current.get_previous()
                i -= 1
        return current.get_data()

    def __remove(self, node):
        """
        Private helper method to remove node from DLL

        Args:
            node(Node): Node to be removed from DLL

        Return:
            Value of removed node

        Raises:
        """
        predecessor = node.get_previous()
        successor = node.get_next()
        predecessor.set_next(successor)
        successor.set_previous(predecessor)
        self.__length -= 1
        return node.get_data()

    def remove_first(self):
        """
        Removes first node in DLL

        Args:

        Return:
            Value of removed node

        Raises:
            ValueError: Empty DLL
        """
        if self.is_empty():
            raise ValueError('Empty DLL')
        return self.__remove(self.__header.get_next())

    def remove_last(self):
        """
        Removes last node in DLL

        Args:

        Return:
            Value of removed node

        Raises:
            ValueError: Empty DLL
        """
        if self.is_empty():
            raise ValueError('Empty DLL')
        return self.__remove(self.__trailer.get_previous())    
        
    def delete_at_index(self, index):
        """
        Delete node at specified index

        Args:
            index(int): Index of node to be deleted
        
        Return:

        Raises:
        """
        if index > self.size() or index < 0:
            raise ValueError('Index out of bounds')
        
        if index == 0:
            return self.remove_first()

        if index == self.size() - 1:
            return self.remove_last()

        i, current = -1, None
        if index < self.size() // 2:
            i, current = 0, self.__header.get_next()
            while current and i != index:
                current = current.get_next()
                i += 1
        else:
            i, current = self.size() - 1, self.__trailer.get_previous()
            while current and i != index:
                current = current.get_previous()
                i -= 1
        return self.__remove(current) 

    def delete(self, value):
        """
        Delete node with specified value from DLL

        Args:
            value: Value of node to delete from DLL

        Return:
            Value of deleted node

        Raises:
            ValueError: Value not in DLL or DLL empty
        """
        # If the list is empty
        if self.is_empty():
            raise ValueError('Value not in DLL and DLL is empty')
        # Traverse DLL to find value
        current = self.__header.get_next()
        while current and current.get_data() != value:
            current = current.get_next()
        # If we are at end of DLL and value not found
        if current == None:
            raise ValueError('Value not in DLL')
        # If we found the value then delete the node
        return self.__remove(current)
    
    def __str__(self):
        """
        String representation of DLL

        Args:

        Return:
            String representation of DLL

        Raises:
        """
        stringrep, current = '', self.__header.get_next()
        while current.get_next() != None:
            stringrep += '<- {} ->'.format(current.get_data())
            current = current.get_next()
        return stringrep
    
    def __iter__(self):
        """
        Returns linked list iterator
        """
        # Remember, self is our UnorderedList.
        # In order to get to the first Node, we must do
        current = self.__header.get_next()
        # and then, until we have reached the end:
        while current.get_next() is not None:
            yield current.get_data()
            # in order to get from one Node to the next one:
            current = current.get_next()
    
    def __next__(self):
        """
        Returns next node's value in DLL.

        1. Define myiter = mydll.__iter__()
        2. print(next(myiter))
        """
        if self.__current == None:
            raise StopIteration
        value = self.__current.get_data()
        self.__current = self.__current.get_next()
        return value

    class Node:
        """
        Inner class representing node in DLL

        Attributes:

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

mydll = DoublyLinkedList()
mydll.add_at_head('William')
print(mydll.size())
print(mydll.last())
mydll.add_at_head('Benjamin')
print(mydll.first())
print(mydll.last())
mydll.add_at_tail('Zion')
print(mydll.last())
print(mydll.size())
mydll.remove_last()
print(mydll.last())
mydll.remove_first()
print(mydll.last())
mydll.remove_last()
mydll.add_at_index('Selena', 0)
mydll.add_at_tail('Andy')
mydll.add_at_tail('Vivian')
mydll.add_at_tail('Jax')
mydll.add_at_tail('Bennett')
mydll.add_at_tail('Cole')
print(mydll.first())
print(mydll.last())
mydll.add_at_index('Jemimah', 3)
print(mydll.__str__())
print(mydll.get_by_index(mydll.size() - 1))
mydll.delete_at_index(mydll.size() - 1)
print(mydll.__str__())
mydll.delete('Selena')
print(mydll.__str__())
mydll.add_at_tail('River')
print(mydll.__str__())
print('Last node: {}'.format(mydll.last()))
# Iterating with iterator since DLL is Iterable
for node in mydll:
    print('Iterating with iterator: {}'.format(node))
# Iterating with __iter__ and __next__
myiter = mydll.__iter__()
for i in range(mydll.size()):
    print('Iterating with next: {}'.format(next(myiter)))
print(mydll.__str__())
print(mydll.last())