class Node:
    """
    Class representing node in unrolled linked list

    Attributes:
        next(Node): Pointer to next node in unrolled linked list
        numElements(int): Number of elements in list
        elements(list): List containing elements stored in node
    """
    def __init__(self):
        self.next = None
        self.numElements = 0
        self.elements = []

class UnrolledLinkedList:
    """
    Class representing unrolled linked list. It is a linear 
    data structure and a variant of the linked list. It 
    stores multiple elements at a node, unlike a regular 
    linked list that contains only a single value. In 
    other words, it is a linked list that stores an array 
    of elements. An unrolled linked list is a combination 
    of an array and a linked list, and thus, it has the 
    advantages of both data structures. It has a small 
    memory overhead (a benefit of an array) and efficient 
    insertion and deletion operations (benefits of a 
    linked list). Unrolled Linked Lists are observed to 
    give better performance than singly-linked lists 
    because of the cache behavior. However, the overhead 
    per node is more as compared to the ordinary linked list.

    Each node in the unrolled linked list contains three 
    types of information: an array containing values, 
    array length, and the pointer to the next node.

    Each array in a node can hold a certain number of 
    elements. Let us call it the capacity. However, 
    typically, it is not filled to its maximum capacity. 
    Generally, the length of each array in a node is equal 
    to the minimum threshold, i.e.,

    Minimum threshold = capacity/2 (integer division)

    Moreover, the unrolled linked list has two pointers: head 
    and tail. Head points to the first node, and tail 
    refers to the last node.
    """
    def __init__(self, capacity):
        """Initializes variables associated with ULL"""
        self.maxElements = capacity
        self.head = None
        self.tail = None

    def isEmpty(self):
        """Method to check if unrolled linked list is empty"""
        return self.head == None

    def insert(self, value):
        """
        If the list is empty, i.e., head = null, then the 
        value to be inserted is the first value. We create 
        a node and add the given value to that node's array. 
        The array length gets increased by 1—both the head 
        and the tail point to this node.

        If the list is not empty, we check if the current 
        node's array can fit a new node. If it can, we append 
        the given value to the current node's array and increase 
        its length by 1. Otherwise, we create a new node. We 
        move half of the elements from the current node to the 
        new node such that the length of the current node is 
        equal to the minimum threshold. We add the given value 
        to the new node and set its length. We also need to 
        update the current node's length. Moreover, we set the 
        current node's next pointer to refer to the new node 
        and also update the tail to point to the new node.

        Params:
            value(int): Value to insert into ULL
        """
        # Case 1. ULL is empty
        if self.isEmpty():
            self.head = Node()
            self.head.elements.append(value)
            self.head.numElements += 1
            self.tail = self.head

        # Case 2: Current node's maxElements is not full
        elif self.tail.numElements + 1 <= self.maxElements:
            self.tail.elements.append(value)
            self.tail.numElements += 1
        
        # Case 3: Current node's maxElements is full
        else:
            newNode = Node() # Create a new node
            # Move final half of elements from the current node to the new node.
            halfLength = self.tail.numElements // 2
            newNode.elements.extend(self.tail.elements[halfLength:])
            newNode.elements.append(value) # Add given value to the new node
            newNode.numElements = len(newNode.elements) # Set the number of elements in the new node
            self.tail.numElements = halfLength # Update the number of elements of the current node
            self.tail.next = newNode # Make current node's next pointer refer to the new node
            self.tail = newNode # Update the tail
    
    def getElementAtPosition(self, position):
        """Method to return element at given position in unrolled linked list"""
        if position < 0:
            raise IndexError('Position out of bounds')
        
        index, current = 0, self.head
        # Traverse unrolled linked list in search of position
        while current is not None:
            for i in range(current.numElements):
                if index == position:
                    return current.elements[i]
                index += 1
            current = current.next
        # Raise error as position is out of bounds
        raise IndexError('Position out of bounds')

    def getElementAtPosition2(self, position):
        """Method to get element at given position more efficiently"""    
        if position < 0:
            raise IndexError('Position out of bounds')
        
        current, index = self.head, 0
        while current is not None:
            if position == index:
                return current.elements[index % self.maxElements]
            elif position < current.numElements:
                return current.elements[position]
            elif position >= current.numElements:
                index += current.numElements
                current = current.next
        raise IndexError('Position out of bounds')

    def __str__(self):
        """Method to return string representation of ULL"""
        outputstr, current = '', self.head
        while current:
            print("numElements: {}".format(current.numElements))
            for i in range(current.numElements):
                outputstr += str(current.elements[i]) + ' '
            outputstr += '\n'
            current = current.next
        return outputstr
        
ull = UnrolledLinkedList(3)
ull.insert(1)
ull.insert(3)
ull.insert(2)
ull.insert(5)
ull.insert(8)
ull.insert(4)
ull.insert(7)
ull.insert(2)
print(ull)
print(ull.getElementAtPosition2(3))