class RecursiveSinglyLinkedList:
    """
    Class representing linked list data type in python
    """
    def __init__(self):
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

    def add_at_head(self, value):
        """
        Associate the specified value with a new node and
        add it to the head of the linked list

        Args:
            value: Value to add to head of linked list

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
            self.__recursive_add_at_tail_helper_function(value, self.__tail)
        self.__length += 1

    def __recursive_add_at_tail_helper_function(self, value, current_node):
        """
        Helper function for add at tail method

        Args:
            value: Value to be associated with node
            current_node(Node): Node we are currently at

        Return:

        Raises:
        """
        # Base case: If we are at the end of the linked 
        if current_node.get_next() == None:
            new_tail = self.Node(value)
            current_node.set_next(new_tail)
            self.__tail = new_tail
            return
        
        # Inductive step
        self.__recursive_add_at_tail_helper_function(value, current_node.get_next())
    
    def add_at_index(self, value, index):
        """
        """
        self.__recursive_add_at_index_helper_function(value, index, None, self.__head)

    def __recursive_add_at_index_helper_function(self, value, index, previous, current):
        """
        """
        # Base case: Index out of bounds
        if index < 0 or index > self.size():
            raise ValueError('Index out of bounds')
        # Base case: Value found at head of linked list
        if index == 0 and current == self.__head:
            self.add_at_head(value)
            return value
        # Base case: Value found at tail of linked list
        if index == 0 and current == self.__tail:
            self.add_at_tail(value)
            return value
        # Base case: Value found at index
        if index == 0:
            new_node = self.Node(value, previous.get_next())
            previous.set_next(new_node)
            self.__length += 1
            return value
        # Inductive step
        self.__recursive_add_at_index_helper_function(value, index - 1, current, current.get_next())

    def delete(self, value):
        """
        Delete specified value from linked list
        """
        self.__recursive_delete_helper_function(value, None, self.__head)

    def __recursive_delete_helper_function(self, value, previous, current):
        """
        Recursive helper function for delete method

        Args:
            value: Value to be deleted
            current(Node): Current node in linked list
            previous(Node): Previous node in linked list

        Return:
            Deleted value

        Raises:
        """
        # Base case: Value not found 
        if current == None:
            return
        # Base case: Delete head
        if value == self.__head.get_value():
            self.__head = current.get_next()
            self.__length -= 1
            return value
        # Base case: Value found
        if current.get_value() == value:
            previous.set_next(current.get_next())
            if current == self.__tail:
                self.__tail = previous
            self.__length -= 1
            return value
        self.__recursive_delete_helper_function(value, current, current.get_next())

    def __recursive_str_helper_function(self, node):
        """
        Recursive helper function for __str__ method

        Args:
            node: Current node to get string representation of

        Return:
            String representation of linked list

        Raises:
        """
        # Base case
        if node.get_next() == None:
            return str(node.get_value())

        # Inductive step
        return str(node.get_value()) + ' -> ' + self.__recursive_str_helper_function(node.get_next())

    def __str__(self):
        """
        Returns string representation of linked list

        Args:

        Return:
            String representation of linked list

        Raises:
        """
        return self.__recursive_str_helper_function(self.__head)

    def contains(self, value):
        """
        Returns boolean indicating if value is in linked list
        """
        return self.__recursive_contains_helper_function(value, self.__head)

    def __recursive_contains_helper_function(self, value, node):
        """
        Recursive helper function for contains method

        Args:
            value: Value to check for in linked list
            node: Current node we are at in the linked list

        Return:
            Boolean indicating if value is in list

        Raises:
        """
        # Base case: Value is not in linked list
        if node == None:
            return False

        # Base case: Value is in linked list
        if node.get_value() == value:
            return True

        # Inductive step
        return self.__recursive_contains_helper_function(value, node.get_next())

    def reverse(self):
        """
        Reverses the order of the linked list

        Args:

        Return:

        Raises:
        """
        self.__head = self.__recursive_reverse_helper_function(self.__head)
    
    def __recursive_reverse_helper_function(self, node):
        """
        Recursive helper function for reverse method

        Args:
            previous(Node): Node preceding current node
            current(Node): Current node
        
        Return:
            Pointer to reversed linked list

        Raises:
        """
        # If head is empty or has reached the list end
        if node is None or node.get_next() is None:
            return node
 
        # Reverse the rest list
        rest = self.__recursive_reverse_helper_function(node.get_next())
 
        # Put first element at the end
        node.get_next().set_next(node)
        node.set_next(None)
 
        # Fix the header pointer
        return rest

    class Node:
        """
        Inner class to represent nodes in RecursiveSinglyLinkedList

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

myrsll = RecursiveSinglyLinkedList()
myrsll.add_at_tail(1)
myrsll.add_at_tail(2)
myrsll.add_at_tail(3)
myrsll.add_at_tail(4)
print(myrsll.size())
print(myrsll.__str__())
for i in range(myrsll.size()):
    print(myrsll.contains(i + 1))
print(myrsll.contains(100))
myrsll.add_at_head('William')
print(myrsll.__str__())
print(myrsll.size())
print(myrsll.__str__())
myrsll.add_at_index('Jefferson', 5)
print(myrsll.__str__())
myrsll.delete('William')
print(myrsll.__str__())
print(myrsll.first())
myrsll.delete(3)
print(myrsll.__str__())
myrsll.delete('Jefferson')
print(myrsll.__str__())
print(myrsll.last())
myrsll.add_at_head('Jericho')
print(myrsll.__str__())
myrsll.add_at_tail('Juno')
print(myrsll.__str__())
myrsll.reverse()
print(myrsll.__str__())
