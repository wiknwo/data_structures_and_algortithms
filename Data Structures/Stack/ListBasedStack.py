class ListBasedStack:
    """Class representing list-based stack in python

    Attributes:
        stack(List): Auxiliary list data structure used to implement list-based stack

    Methods:
        is_empty(): Returns boolean indicating whether stack is empty O(1)
        size(): Returns size of the stack O(1)
        top(): Returns value of the top most element of the stack O(1)
        push(item): Pushes item onto the top of the stack O(1)
        pop(): Deletes the topmost item of the stack O(1)
    """

    def __init__(self):
        """Initializes stack with empty list"""
        self.__stack = []

    def is_empty(self):
        """Returns boolean indicating if the stack is empty"""
        return len(self.__stack) == 0
    
    def size(self):
        """Returns number of items in stack"""
        return len(self.__stack)
    
    def top(self):
        """Returns topmost item on stack"""
        return self.__stack[-1]
    
    def push(self, item):
        """Pushes item onto top of stack"""
        self.__stack.append(item)
    
    def pop(self):
        """Removes and returns topmost item from stack"""
        return self.__stack.pop()

    def __str__(self):
        """Return string representation of stack"""
        return self.__stack.__str__()
            
### Testing ###
mystack = ListBasedStack()
mystack.push('Jordan')
mystack.push('Benedict')
mystack.push('Angelica')
mystack.push('Leslie')
print("Top(): {}".format(mystack.top()))
print("Pop(): {}".format(mystack.pop()))
print("IsEmpty(): {}".format(mystack.is_empty()))
print("Size(): {}".format(mystack.size()))

print(mystack)