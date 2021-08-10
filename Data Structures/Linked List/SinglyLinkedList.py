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
        self.__current_node = self.__head # Pointer to current node for iterator
    
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
        
        if index == 0:
            return self.__head.get_value()

        if index == self.size() - 1:
            return self.__tail.get_value()

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
                if i == self.size() - 1:
                    self.__tail = previous_node
                self.__length -= 1
                return value
            previous_node = current_node
            current_node = current_node.get_next()
            i = i + 1
    
    def delete(self, value):
        """
        Delete the specified value from the linked list

        Args:
            value: Value to be deleted

        Return:
            Value that was deleted

        Raises:
            ValueError: Value not in list or list is empty
        """
        # If the list is empty
        if self.is_empty():
            raise ValueError('Value not in linked list and linked list is empty')

        # If we are deleting the head
        if self.__head.get_value() == value:
            self.__head = self.__head.get_next()
            self.__length -= 1
            return value 

        # Traverse linked list
        previous_node, current_node = None, self.__head
        while current_node != None and current_node.get_value() != value:
            previous_node = current_node
            current_node = current_node.get_next()
        
        # If we are at the end of the linked list
        # and we have not found the value
        if current_node == None:
            raise ValueError('Value not in linked list')
        
        # If we found the value then delete the node
        previous_node.set_next(current_node.get_next())
        if current_node == self.__tail:
            self.__tail = previous_node
        self.__length -= 1
        return value
    
    def removeFirst(self):
        """
        Delete the first value in the linked list

        Args:

        Return:
            The value of the first node
        
        Raises:
        """
        return self.delete_at_index(0)

    def removeLast(self):
        """
        Delete the last value in the linked list

        Args:

        Return:
            The value of the last node
        
        Raises:
        """ 
        return self.delete_at_index(self.size() - 1)

    def contains(self, value):
        """
        Checks if value is contained in node in linked list

        Args:
            value: Value to check for in linked list

        Return:
            Boolean indicating if value in linked list

        Raises:
        """
        i = 0
        current_node = self.__head
        while current_node and i < self.__length:
            if current_node.get_value() == value:
                return True
            current_node = current_node.get_next()
            i += 1
        return False

    def floyds_cycle_finding_algorithm(self):
        """
        Algorithms finds cycle in linked list if it exists

        Args:

        Return:
            Boolean indicating if there is a cycle

        Raises:
        """
        slow_pointer = fast_pointer = self.__head
        while slow_pointer and fast_pointer and fast_pointer.get_next():
            slow_pointer = slow_pointer.get_next()
            fast_pointer = fast_pointer.get_next().get_next()
            if slow_pointer == fast_pointer:
                return True
        return False   

    def sort(self):
        """
        Sort list in ascending order

        Args:

        Return:

        Raises:
        """
        current_node, tmp = self.__head, []
        # Add values in linked list to standard list
        while current_node:
            tmp.append(current_node.get_value())
            current_node = current_node.get_next()
        # Sort the standard list
        tmp.sort()
        # Recreate linked list
        new_sll = self.Node() # Create new node
        current_node = new_sll # Set current to new node
        for item in tmp:
            current_node.set_next(self.Node(item))
            current_node = current_node.get_next()
        self.__head = new_sll.get_next() # Head of new list is node following this one



    def get_midpoint(self):  
        """
        Traverse linked list using two pointers. Move one 
        pointer by one and the other pointers by two. When 
        the fast pointer reaches the end slow pointer will 
        reach the middle of the linked list. This is 
        because the fast pointer is moving twice as fast
        and thus should get to the end in half the time.

        Args:

        Return:
            Middle node of linked list
        
        Raises:
        """  
        slow_pointer, fast_pointer = self.__head, self.__head
        while fast_pointer and fast_pointer.get_next():
            slow_pointer = slow_pointer.get_next()
            fast_pointer = fast_pointer.get_next().get_next()
        return slow_pointer.get_value()

    def __iter__(self):
        """Iterator for linked list

        Args:

        Return:
            self
        
        Raises:
        """
        # Remember, self is our UnorderedList.
        # In order to get to the first Node, we must do
        current = self.__head
        # and then, until we have reached the end:
        while current is not None:
            yield current.get_value()
            # in order to get from one Node to the next one:
            current = current.get_next()

    def __next__(self):
        """Gets the next element in the linked list

        Args:

        Return:
            Next element in linked list
        
        Raises: 
            StopIteration
        """
        if self.__current_node == None:
            raise StopIteration
        value = self.__current_node.get_value()
        self.__current_node = self.__current_node.get_next()
        return value

    def __str__(self):
        """
        String representation of linked list

        Args:

        Return:
            String representation of linked list

        Raises:
        """
        stringrep = ''
        current_node = self.__head
        while current_node.get_next() != None:
            stringrep += current_node.get_value() + ' -> '
            current_node = current_node.get_next()
        stringrep += current_node.get_value()
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

mysll = SinglyLinkedList()
mysll.add_at_tail('William')
mysll.add_at_tail('Vanessa')
mysll.add_at_head('Merissa')
mysll.add_at_tail('Winnifred')
mysll.delete('Winnifred')
print(mysll.__str__())
for value in mysll:
    print('iter: {}'.format(value))
my_iter = iter(mysll)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
mysll.add_at_tail('Winnifred')
print(mysll.__str__())
print(mysll.size())
for i in range(mysll.size()):
    print('i = {}: {}'.format(i, mysll.get_by_index(i)))
print(mysll.last())
print(mysll.first())
print(mysll.last())
print(mysll.get_by_index(1))
mysll.add_at_index(1, 'Zarathustra')
print(mysll.get_by_index(1))
print(mysll.size())
print(mysll.delete_at_index(mysll.size() - 1))
print(mysll.__str__())
print(mysll.contains('William'))
mysll.delete('Zarathustra')
for i in range(mysll.size()):
    print('i = {}: {}'.format(i, mysll.get_by_index(i)))
print(mysll.size())
mysll.add_at_tail('Wolfgang')
print(mysll.removeFirst())
mysll.add_at_tail('Benjamin')
for i in range(mysll.size()):
    print('i = {}: {}'.format(i, mysll.get_by_index(i)))
print(mysll.removeLast())
mysll.add_at_tail('Winnifred')
print(mysll.__str__())
print(mysll.floyds_cycle_finding_algorithm())
for i in range(mysll.size()):
    print('i = {}: {}'.format(i, mysll.get_by_index(i)))
mysll.add_at_tail('Ikenna')
print(mysll.__str__())
print(mysll.last())
print(mysll.size())
for i in range(mysll.size()):
    print('i = {}: {}'.format(i, mysll.get_by_index(i)))
print(mysll.get_midpoint())
mysll.sort()
print(mysll.__str__())
print(mysll.add_at_head.__doc__)