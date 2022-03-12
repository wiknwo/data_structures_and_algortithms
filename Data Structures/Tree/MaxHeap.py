class MaxHeap:
    """
    Class represnting a Maxiumum Heap using a list as an auxiliary data structure
    A heap is a complete binary tree that stores keys (key-value pairs) at its 
    internal nodes and that satisfies two additional properties;
        
        - Order Property: key(parent) >= key(child) in the case of max heap or vice versa for min heap.
        - Structural “Completeness” Property: all levels are full, except the bottom, which is “left-filled”.
        Rule 1: Level i has 2^i nodes, for 0 <= i < h where h is the height of the tree
        Rule 2: At level h-1, all leafs are to right of all internal nodes

        A heap storing N keys has height; h = ceiling(log(N + 1))

    - root node index: i = 0
    - parent node index: (i - 1) / 2
    - left child index: 2 * i + 1
    - right child index: 2 * i + 2
    """
    def __init__(self):
        """Initializes MaxHeap with list as auxiliary data structure"""
        self.__heap = []
    
    def is_empty(self):
        """Method to check if MaxHeap is empty"""
        return len(self.__heap) == 0

    def size(self):
        """Method to return size of max heap"""
        return len(self.__heap)

    def __swap(self, i, j):
        """Helper method to swap two nodes in MaxHeap"""
        self.__heap[i], self.__heap[j] = self.__heap[j], self.__heap[i]
    
    def peek(self):
        """Method to return root of MaxHeap which is also the maximum element"""
        if self.is_empty():
            raise ValueError('MaxHeap is empty!')
        return self.__heap[0]

    def poll(self):
        """Method to remove and return the root of the MaxHeap i.e. the maximum element"""
        if self.is_empty():
            raise ValueError('MaxHeap is empty!')            
        minimum_element = self.__heap[0]
        self.__heap[0] = self.__heap[len(self.__heap) - 1]
        del self.__heap[len(self.__heap) - 1]
        self.__downheap(0)
        return minimum_element

    def insert(self, element):
        """Method to insert data into a new node in the MaxHeap"""
        self.__heap.append(element)
        self.__upheap(len(self.__heap) - 1)

    def __upheap(self, node_index):
        """
        Helper method to restore the “order property”. This involves 
        repeatedly swapping the newly added entry with parent entries 
        until the property is restored.
        """
        # Base case / stopping condition
        # Upheap terminates when new value is less than the value 
        # of its parent, or the top of the heap is reached.
        if node_index == 0 or self.__heap[node_index] <= self.__heap[(node_index - 1) // 2]:
            return
        else:
            self.__swap(node_index, (node_index - 1) // 2) # The parent is less than the child so swap to maintain ordering
            # Inductive step: Do some work to shrink the problem space
            self.__upheap((node_index - 1) // 2) # Check if the order property is maintained at the parent node

    def __downheap(self, node_index):
        """
        Helper method performs a downheap to re-establish the “ordering property”. 
        This involves checking whether the given node is greater than its children. 
        If it is not, then the node is swapped with the greater of the two children, 
        and downheap is performed again on the node in its new position.
        """
        # Checking if this node has left and right children
        if 2 * node_index + 1 < self.size() and 2 * node_index + 2 < self.size():
            if self.__heap[2 * node_index + 1] > self.__heap[2 * node_index + 2]:
                self.__swap(node_index, 2 * node_index + 1) # Swap the left child with the current node since it is > current node
                self.__downheap(2 * node_index + 1)
            else:
                self.__swap(node_index, 2 * node_index + 2) # Swap the right child with the current node since it is < current node
                self.__downheap(2 * node_index + 2)
        elif 2 * node_index + 1 < self.size() and self.__heap[node_index] < self.__heap[2 * node_index + 1]:
            self.__swap(node_index, 2 * node_index + 1) # Swap the left child with the current node since it is > current node
            self.__downheap(2 * node_index + 1)
        elif 2 * node_index + 2 < self.size() and self.__heap[node_index] < self.__heap[2 * node_index + 2]:
            self.__swap(node_index, 2 * node_index + 2) # Swap the right child with the current node since it is > current node
            self.__downheap(2 * node_index + 2)

    def __str__(self):
        """Method to return string representation of minheap"""
        minheapstr, left_child, right_child = '', None, None
        for i in range(self.size() // 2):
            if 2 * i + 1 < self.size():
                left_child = self.__heap[2 * i + 1]
            if 2 * i + 2 < self.size():
                right_child = self.__heap[2 * i + 2]
            minheapstr += "Parent: {} | Left child: {} | Right child: {}\n".format(self.__heap[i], left_child, right_child)
            left_child, right_child = None, None
        return minheapstr

maxheap = MaxHeap()
maxheap.insert(5)
maxheap.insert(3)
maxheap.insert(17)
maxheap.insert(10)
maxheap.insert(84)
maxheap.insert(19)
maxheap.insert(6)
maxheap.insert(22)
maxheap.insert(9)

while not maxheap.is_empty():
    print(maxheap)
    print("The maximum value is: {}".format(maxheap.poll()))
