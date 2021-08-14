class CircularlyLinkedList:
    """
    Class representing link-based circularly linked list in python
    """
    def __init__(self):
        """
        Initializes CLL
        """
        self.__head = None
        self.__length = 0

    def size(self):
        """
        Returns size of CLL
        """
        return self.__length
    
    def is_empty(self):
        """
        Returns boolean indicating if CLL is empty
        """
        return self.__length == 0
    
    def first(self):
        """
        Returns value of node at head of CLL
        """
        if self.is_empty():
            raise ValueError('CLL is empty')
        return self.__head.get_value()
    
    def last(self):
        """
        Returns value of last node of CLL
        """
        if self.is_empty():
            raise ValueError('CLL is empty')
        current = self.__head
        while current.get_next() != self.__head:
            current = current.get_next()
        return current.get_value()
        
    def add_at_head(self, value):
        """
        Add new node with value to CLL at head
        """
        new_node = self.Node(value, self.__head)
        current = self.__head
        # If list is not empty set next of last node
        if not self.is_empty():
            while current.get_next() != self.__head:
                current = current.get_next()
            current.set_next(new_node)
        else:
            new_node.set_next(new_node)
        self.__head = new_node
        self.__length += 1
    
    def add_at_tail(self, value):
        """
        Add a new node with value at the second to last position
        in CLL
        """
        if self.is_empty():
            new_node = self.Node(value)
            new_node.set_next(new_node)
            self.__head = new_node
        else:
            current = self.__head
            while current.get_next() != self.__head:
                current = current.get_next()
            new_node = self.Node(value, self.__head)
            current.set_next(new_node)
        self.__length += 1

    def add_at_index(self, value, index):
        """
        Add new node with value at specified index in CLL
        """
        if index > self.size() or index < 0:
            raise IndexError('Index out of bounds')
        
        if index == 0:
            return self.add_at_head(value)
        
        if index == self.__length:
            return self.add_at_tail(value)
    
        i, previous, current = 0, self.__head, self.__head
        while current.get_next() != self.__head and i < self.__length:
            if i == index:
                new_node = self.Node(value, previous.get_next())
                previous.set_next(new_node)
                self.__length += 1
                return 
            previous = current
            current = current.get_next()
            i += 1
        
        # If we are at the end of the CLL then index is
        # end of CLL
        if current.get_next() == self.__head:
            new_node = self.Node(value, previous.get_next())
            previous.set_next(new_node)
            self.__length += 1

    def delete(self, value):
        """
        Delete node with value from CLL
        """
        # If CLL is empty
        if self.is_empty():
            raise ValueError('CLL is empty')
        # If CLL contains only one node
        if self.__head.get_value() == value and self.__head.get_next() == self.__head:
            self.__head = None
            return
        # If CLL contains more than one node
        current = self.__head
        # If head is to be deleted
        if self.__head.get_value() == value:
            return self.remove_first()
        # Traverse list till end reached or value found
        while current.get_next() != self.__head and current.get_next().get_value() != value:
            current = current.get_next()
        # If node to be deleted found
        if current.get_next().get_value() == value:
            current.set_next(current.get_next().get_next())
            self.__length -= 1
        else:
            raise ValueError('Value not in CLL')

    def remove_first(self):
        """
        Delete first node of CLL
        """
        # If CLL is empty
        if self.is_empty():
            raise ValueError('CLL is empty')
        # Define pointers 
        previous_node, next_node = self.__head, self.__head
        # If CLL has single node
        if previous_node.get_next() == previous_node:
            self.__head = None
            self.__length -= 1
            return
        # Traverse list keeping track of 
        # next and previous nodes
        while previous_node.get_next() != self.__head:
            previous_node = previous_node.get_next()
            next_node = previous_node.get_next()
        # Now previous is last node and
        # next is first node of list
        # first node(next) link address
        # put in last node(previous) link
        previous_node.set_next(next_node.get_next())
        # Make second node the head node
        self.__head = previous_node.get_next()
        self.__length -= 1

    def remove_last(self):
        """
        Delete last node of CLL
        """
        if self.is_empty():
            raise ValueError('CLL is empty')
        previous, current = None, self.__head
        # Check if there is a single node
        # in the CLL
        if current.get_next() == current:
            self.__head = None
            self.__length -= 1
            return
        # Traverse the CLL
        while current.get_next() != self.__head:
            previous = current
            current = current.get_next()
        # Make the second last node the new head
        previous.set_next(current.get_next())
        self.__head = previous.get_next()
        self.__length -= 1
    
    def delete_at_index(self, index):
        """
        Delete node at specified index in CLL
        """
        if self.is_empty():
            raise Exception('CLL is empty')
        
        if index >= self.size() or index < 0:
            raise IndexError('Index out of bounds')
        
        if index == 0:
            return self.remove_first()
        
        if index == self.size() - 1:
            return self.remove_last()
        
        previous, current, i = self.__head, self.__head, 0
        while current and i < self.__length:
            if i == index:
                value = current.get_value()
                previous.set_next(current.get_next())
                self.__length -= 1
                return value
            previous = current
            current = current.get_next()
            i += 1

    def floyds_cycle_finding_algorithm(self):
        """
        Algorithms finds cycle in linked list if it exists
        """
        slow_pointer = fast_pointer = self.__head
        while slow_pointer and fast_pointer and fast_pointer.get_next():
            slow_pointer = slow_pointer.get_next()
            fast_pointer = fast_pointer.get_next().get_next()
            if slow_pointer == fast_pointer:
                return True
        return False   

    def __str__(self):
        """
        Return string representation of CLL
        """
        stringrep, current = '', self.__head
        while current.get_next() != self.__head:
            stringrep += '{} -> '.format(current.get_value())
            current = current.get_next()
        stringrep += '{} -> Back to head'.format(current.get_value())
        return stringrep

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

mycll = CircularlyLinkedList()
mycll.add_at_head('William')
mycll.add_at_head('Bernard')
mycll.add_at_head('Dwayne')
print(mycll.__str__())
print(mycll.first())
print(mycll.last())
print(mycll.floyds_cycle_finding_algorithm())
mycll.remove_first()
print(mycll.first())
print(mycll.last())
mycll.delete('William')
print(mycll.first())
print(mycll.last())
print(mycll.size())
print(mycll.__str__())
mycll.add_at_head('William')
print(mycll.__str__())
mycll.add_at_head('Rodrick')
mycll.add_at_head('Benedict')
mycll.add_at_head('Emilia')
mycll.add_at_head('Rita')
print(mycll.__str__())
mycll.remove_last()
print(mycll.__str__())
print(mycll.size())
mycll.delete_at_index(3)
print(mycll.__str__())
print(mycll.last())
mycll.add_at_tail('Bianca')
print(mycll.__str__())
mycll.delete('Bianca')
print(mycll.__str__())
mycll.add_at_index('Jeffrey', 2)
print(mycll.__str__())
mycll.add_at_index('Augustine', 4)
print(mycll.__str__())
mycll.add_at_index('Sylvestre', 5)
print(mycll.__str__())
mycll.add_at_index('Valentina', 7)
print(mycll.__str__())
mycll.delete_at_index(7)
print(mycll.__str__())
mycll.remove_first()
print(mycll.__str__())
