'''Class representing dynamic array data type in python using lists
'''
class DynamicArray:
    def __init__(self, capacity = 16):
        """Initialises dynamic array with specified capacity. Default is 16 if no capacity is given.

        Args:
            capacity(int): The number of elements array should be able to store
        
        Return:
        
        Raises: 
            ValueError: Capacity must be greater than or equal to 0
        """
        # Checking if capacity is out of bounds
        if capacity < 0:
            raise ValueError('Capacity must be greater than or equal to 0')
        self.__capacity = capacity
        self.__array = [None] * self.__capacity # Our dynamic array auxiliary data structure, a list.
        self.__len = 0 # The length the user thinks the array is.
        self.__index = 0 # Index for iterator

    def size(self):
        """Gets size of the dynamic array

        Args:

        Return:
            Number of elements in dynamic array

        Raises:
        """
        return self.__len
    
    def __iter__(self):
        """Iterator for dynamic array

        Args:

        Return:
            self
        
        Raises:
        """
        return self

    def __next__(self):
        """Gets the next element in the dynamic array

        Args:

        Return:
            Next element in dynamic array
        
        Raises: 
            StopIteration
        """
        if self.__index >= self.size():
            raise StopIteration
        index = self.__index
        self.__index += 1
        return self.__array[index]
    
    def is_empty(self):
        """Checks if dynamic array contains no elements

        Args:
        
        Return:
            Boolean indicating if array is empty or not
        
        Raises:
        """
        return self.size() == 0

    def get(self, index):
        """Gets the value at the specified index in the dynamic array

        Args: 
            index(int): index of element in array
        
        Return:
            Element at index
            
        Raises:
            ValueError: Index out of bounds
        """
        if index < 0 or index >= self.size():
            raise ValueError('Index out of bounds')
        return self.__array[index]

    def set(self, index, element):
        """Update the element at the specified index with a new element

        Args:
            index(int): Index of element
            element: New element to be placed at specified index
        
        Return:

        Raises:
            ValueError: Index out of bounds
        """
        if index < 0 or index >= self.size():
            raise ValueError('Index out of bounds')
        self.__array[index] = element
    
    def clear(self):
        """Remove all elements from the dymanic array

        Args:

        Return:
        
        Raises:
        """
        for i in range(self.__capacity):
            self.__array[i] = None
        self.__len = 0 # Reset the length of the dynamic array

    def add(self, element):
        """Add an element to the end of the dynamic array

        Args:
            element: Element to be added
        
        Return:

        Raises:
        """
        # Check if you need to resize the dynamic array
        if self.size() + 1 >= self.__capacity:
            if self.__capacity == 0: 
                self.__capacity = 1
            else:
                # Double the capacity of the dynamic array
                self.__capacity *= 2
            # Copy over the elements of the array 
            # from the old one to the new
            # one.
            new_array = [None] * self.__capacity
            for i in range(self.size()):
                new_array[i] = self.__array[i]
            self.__array = new_array
        
        # If no resize if necessary then
        # add the element into the next
        # available index
        self.__array[self.__len] = element
        self.__len += 1 # increment the length of the dynamic array
    
    def remove_at_index(self, index):
        """Remove element at specified index

        Args:
            index(int): Index of element to be removed.

        Return:
            element: Element that was removed

        Raises:
            ValueError: Index out of bounds
        """
        if index < 0 or index >= self.size():
            raise ValueError('Index out of bounds')

        element = self.__array[index] # Copy element to be removed
        new_array = [None] * (self.__len - 1) # Create new dynamic array without element to remove
        i, j = 0, 0 # Indices to traverse old and new array respectively
        while i < self.__len:
            if i == index:
                j -= 1 # Skip over index of element to be removed by fixing j temporarily        
            else:
                new_array[j] = self.__array[i]
            i += 1
            j += 1
        self.__array = new_array
        self.__len -= 1
        self.__capacity = self.__len
        return element
    
    def remove(self, element):
        """Remove specified element from dynamic array

        Args:
            element(int): Element to be removed

        Return:
            Element that was removed if it exists

        Raises:
            ValueError: Element not in dynamic array
        """
        for i in range(self.__len):
            if self.__array[i] == element:
                return self.remove_at_index(i)
        raise ValueError('Element not in dynamic array')

    def index_of(self, element):
        """Gets index of specified element

        Args:
            element: Element to get index of

        Return:
            Index of specified element

        Raises:
            ValueError: Element not in dynamic array
        """
        for i in range(self.size()):
            if self.__array[i] == element:
                return i
        raise ValueError('Element not in dynamic array')
    
    def contains(self, element):
        """Check to see if element is contained in dynamic array

        Args:
            element: Element to be checked

        Return:
            Boolean indicating if element in dynamic array or not
        
        Raises:
        """
        for i in range(self.size()):
            if self.__array[i] == element:
                return True
        return False

    def __str__(self):
        """Provide string representation of dynamic array

        Args:

        Return:
            String representation of dynamic array
        
        Raises:
        """
        if self.is_empty():
            return '[]'
        else:
            stringrep = '['
            for i in range(self.size() - 1):
                stringrep += self.__array[i] + ', '
            stringrep += self.__array[self.size() - 1] + ']'
            return stringrep


