class SinglyLinkedList:
    """
    Class representing linked list data type in python

    Attributes:
        Node(Inner Class): Inner class representing node in linked list.

    Methods:

    """
    def __init__(self):
        """Initialize linked list with head and tail pointers pointing to None

        Args:

        Return:

        Raises:
        """
        self.__head = None # Head node of the linked list (or None if empty)
        self.__tail = None # Last noe of the linked list (or None if empty)
        self.__length = 0 # Number of nodes in the linked list
    
    def size(self):
        """
        Size of linked list

        Args:

        Return:
            Number of values in linked list
        
        Raises:
        """
        return self.__length
    
    def is_empty(self):
        """
        Check if linked list is empty

        Args:

        Return:
            Boolean indicating if linked list is empty

        Raises:
        """
        return self.size() == 0

    def first(self):
        """
        Returns the first element

        Args:

        Return:
            First element of linked list

        Raises:
        """
        if self.is_empty():
            return None
        return self.__head.get_value()

    def last(self):
        """
        Returns last element of the linked list

        Args:

        Return:
            Last element of linked list

        Raises:
        """    
        if self.is_empty():
            return None
        return self.__tail.get_value()

    def get_by_index(self, index):
        """
        Retrieve node value at index

        Args:
            index(int): Index of element to retrieve

        Return:
            Value at index
        
        Raises:
            ValueError: Index out of bounds
        """
        # Check if index is in bounds
        if index < 0 or index >= self.size():
            raise ValueError('Index out of bounds')

        # Traverse linked list to get value at index
        i = 0
        current_node = self.__head
        while current_node and i < self.__length:
            if i == index:
                return current_node.get_value()
            current_node = current_node.get_next()
            i += 1

    def add_at_head(self, value):
        """
        Add a node of value val before the first element 
        of the linked list. After the insertion, the new 
        node will be the first node of the linked list.

        Args:
            value: New value to insert into linked list

        Return:

        Raises:
        """
        self.__head = self.Node(value, self.__head)
        if self.is_empty():
            self.__tail = self.__head
        self.__length += 1

    def add_at_tail(self, value):
        """
        Append a node of value val to the last 
        element of the linked list.

        Args:
            value: Value to associate with new node at end of list

        Return:

        Raises:
        """   
        new_tail = self.Node(value, None)

        # Make the head the tail as well if the linked list is empty
        if self.is_empty():
            self.__head = new_tail
            self.__tail = self.__head
        else:
            self.__tail.set_next(new_tail) # Make the current tail point to the new tail
            self.__tail = new_tail # Make the new tail the current tail
        self.__length += 1
    
    def add_at_index(self, index, value):
        """
        Add a node of value value before the index-th 
        node in the linked list. If index equals to the 
        length of linked list, the node will be appended 
        to the end of linked list. If index is greater 
        than the length, the node will not be inserted.

        Args:
            value: Value to be inserted at specified index
            index(int): Index where value is to be placed 

        Return:

        Raises:
            ValueError: Index out of bounds
        """
        if index > self.__length or index < 0:
            raise ValueError('Index out of bounds')

        if index == 0:
            return self.add_at_head(value)
        
        if index == self.__length:
            return self.add_at_tail(value)

        i = 0
        current_node = previous_node = self.__head
        while current_node and i < self.__length:
            if i == index:
                new_node = self.Node(value, previous_node.get_next())
                previous_node.set_next(new_node)
                self.__length += 1
                return None
            previous_node = current_node
            current_node = current_node.get_next()
            i += 1

    def delete_at_index(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.

        Args:
            index(int): Index of node to be deleted

        Return:
            Value of deleted node

        Raises:
            ValueError: Index out of bounds
        """
        if index >= self.__length or index < 0:
            raise ValueError('Index out of bounds')

        if index == 0:
            value = self.__head.get_value()
            self.__head = self.__head.get_next()
            self.__length -= 1
            return value    
        
        i = 0
        current_node = previous_node = self.__head
        while current_node and i < self.__length:
            if i == index:
                value = current_node.get_value()
                previous_node.set_next(current_node.get_next())
                self.__length -= 1
                return value
            previous_node = current_node
            current_node = current_node.get_next()
            i = i + 1
    
    def contains(self, value):
        i = 0
        current_node = self.__head
        while current_node and i < self.__length:
            if current_node.get_value() == value:
                return True
            current_node = current_node.get_next()
            i += 1
        return False

    class Node:
        """
        Inner class to represent nodes in SinglyLinkedList

        Attributes:
            value: data stored in node
            next: Pointer to node following this one

        Methods:
            get_value(): Returns data stored in node
            get_next(): Returns node following this one
            set_next(node): Sets the node following this one to node
        """

        def __init__(self, value = None, node = None):
            """
            initialize node with value
            
            Args:
                value: Value to associate with node
                next(Node): Pointer to next node in linked list

            Return:

            Raises:
            """
            self.__value = value
            self.__next = node
        
        def get_value(self):
            """
            Returns element at node

            Args:

            Return:
                Element at node

            Raises:
            """
            return self.__value
        
        def get_next(self):
            """
            Returns the node that follows this one or None if no such node

            Args:

            Return:
                The node that follows this one

            Raises:
            """
            return self.__next

        def set_next(self, node):
            """
            Sets the node's next reference to point to node node
            
            Args:
                node(Node): New node for this node's next pointer to reference

            Return:

            Raises:
            """
            self.__next = node

mysll = SinglyLinkedList()
mysll.add_at_tail('William')
mysll.add_at_tail('Vanessa')
mysll.add_at_head('Merissa')
mysll.add_at_tail('Winnifred')
print(mysll.first())
print(mysll.last())
print(mysll.get_by_index(1))
mysll.add_at_index(1, 'Zarathustra')
print(mysll.get_by_index(1))
print(mysll.size())
print(mysll.delete_at_index(mysll.size() - 1))
for i in range(mysll.size()):
    print('i = {}: {}'.format(i, mysll.get_by_index(i)))
print(mysll.contains('William'))