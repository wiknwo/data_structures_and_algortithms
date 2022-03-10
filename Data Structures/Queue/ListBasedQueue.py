class ListBasedQueue:
    """Class representing list-based queue

    Attributes:
        queue(List): Auxiliary list data structure used to implement list-based queue

    Methods:
        enqueue(element): Insert element at the rear of the queue O(1)
        dequeue(): Remove the element from the front of the queue O(1)
        front(): Return a reference to the element at the front of the queue
        size(): Return number of elements in queue
        is_empty(): Return boolean indicating if queue is empty or not
    """

    def __init__(self):
        """Initializes queue with empty list"""
        self.__queue = []
    
    def enqueue(self, element):
        """Insert element at the rear of the queue"""
        self.__queue.append(element)

    def dequeue(self):
        """Remove the element at the front of the queue"""
        return self.__queue.pop(0)
    
    def front(self):
        """Return reference to element at front of queue"""
        return self.__queue[0]

    def size(self):
        """Return number of elements in the queue"""
        return len(self.__queue)
    
    def is_empty(self):
        """Return nolean indicating if queue is empty"""
        return len(self.__queue) == 0
    
    def __str__(self):
        """Return string represntation of queue"""
        return self.__queue.__str__()

### Testing ###
myqueue = ListBasedQueue()
myqueue.enqueue('Benjamin')
myqueue.enqueue('Wolfgang')
myqueue.enqueue('Thumbelina')
myqueue.enqueue('Stacey')
print(myqueue)
print("front(): {}".format(myqueue.front()))
print("dequeue(): {}".format(myqueue.dequeue()))
print("front(): {}".format(myqueue.front()))
print("is_empty(): {}".format(myqueue.is_empty()))
print("size(): {}".format(myqueue.size()))

