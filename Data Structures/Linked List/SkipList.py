import random
class SkipList:
    """
    Class representing skiplist as created by William Pugh

    A skip list is built in layers. The bottom layer is an ordinary ordered 
    linked list. Each higher layer acts as an "express lane" for the lists below, 
    where an element in layer i appears in layer i+1 with some fixed probability p 
    (two commonly used values for p are 1/2 or 1/4). On average, each element appears 
    in 1/(1-p) lists, and the tallest element (usually a special head element at the 
    front of the skip list) in all the lists. The skip list contains log_1/p(n) lists.

    In an ordinary sorted list, insert, delete, and search operations require sequential 
    traversal of the list. This results in O(n) performance per operation. Skip Lists allow 
    intermediate nodes in the list to be skipped during a traversal - resulting in an 
    expected performance of O(log n) per operation.

    Attributes:
        MAX_LEVEL(int): Constant denoting maximum number of levels in skip list
        P(float): Constant denoting fraction of nodes with level i pointers also having level i + 1 pointers
        header(SkipNode): Head of skiplist which is a dummy node
        level(int): Number of levels in skiplist i.e. SkipNode with highest level

    Methods:
        insert(key): Inserts SkipNode with key into skip list
        search(key): Searches for SkipNode with specified key in skip list
        erase(key): Deletes SkipNode with specified key from skip list if it exists
        random_level(): Generates random level at which to insert new SkipNode
    """
    def __init__(self, max_level = 16, p = 0.5):
        """
        Initializes attributes of SkipList with values
        """
        # Maximum level for this skip list
        self.__MAX_LEVEL = max_level

        # P is the fraction of the nodes with level 
        # i references also having level i+1 references
        self.__P = p

        # Create header node and initialize to -1
        self.__header = self.SkipNode(-1, self.__MAX_LEVEL)

        # Current level of skip list
        self.__level = 0

    def random_level(self):
        """
        Before we start inserting the elements in the skip list we need 
        to decide the nodes level.Each element in the list is represented 
        by a node, the level of the node is chosen randomly while insertion 
        in the list. Level does not depend on the number of elements in the node. 
        The level for node is decided by the following algorithm.

        __MAX_LEVEL is the upper bound on number of levels in the skip list. It can 
        be determined as – L(N) = log_p/2(N). This algorithm assures that random level 
        will never be greater than __MAX_LEVEL. Here p is the fraction of the nodes 
        with level i pointers also having level i+1 pointers and N is the number of 
        nodes in the list.
        """
        level = 0
        while random.random() < self.__P and level < self.__MAX_LEVEL:
            level += 1
        return level

    def insert(self, key):
        """
        We will start from highest level in the list and compare key of 
        next node of the current node with the key to be inserted. Basic idea is:

        1. Key of next node of current node is less than key to be inserted 
        then we keep on moving forward on the same level

        2. Key of next node of current node is greater than the key to be inserted 
        then we store the pointer to current node i at update[i] and move one level 
        down and continue our search.

        The insert algorithm maintains two local variables(besides the skip list header):

        - X (current): a pointer which points to a node whose forward pointers point to nodes 
        whose key we are currently comparing to the key we want to insert this lets us quickly 
        compare keys, and follow forward pointers

        - update: an array of node pointers which point to nodes whose forward pointers may need 
        to be updated to point to the newly inserted node, if the new node is inserted in the list 
        just before the node X points to this, lets us quickly update all the pointers necessary to 
        splice in the new node
        """    
        # Here update[i] holds the pointer to node at level i from which we moved down 
        # to level i-1 and pointer of node left to insertion position at level 0.
        update = [None] * (self.__MAX_LEVEL + 1)

        # X (current)
        current = self.__header

        # Start from highest level of skip list move the current reference forward while node next 
        # to current's key is less than key. Otherwise insert current in update and move one level 
        # down and continue search
        for i in range(self.__MAX_LEVEL, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current
        
        # Reached level 0 and forward reference to right is desired position to insert key.
        current = current.forward[0]

        # if current is None that means we have reached to end of the level or if current's key is 
        # not equal to key to insert that means we have to insert node between update[0] and 
        # current node
        if current == None or current.key != key:
            # Generate random level at which we will insert SkipNode
            random_level = self.random_level()

            # If random level is greater than list's current level (node with highest level inserted 
            # in list so far), initialize update value with reference to header for further use
            if random_level > self.__level:
                for i in range(self.__level + 1, random_level + 1):
                    update[i] = self.__header
                self.__level = random_level
            
            # Create new SkipNode with randomly generated level
            new_node = self.SkipNode(key, random_level)

            # Insert node by rearranging pointer references
            for i in range(random_level + 1):
                new_node.forward[i] = update[i].forward[i]
                update[i].forward[i] = new_node

    def search(self, key):
        """
        Searching an element is very similar to the approach for searching for a spot to insert
        an element in the Skip list. The basic idea is as follows;

        1. Key of next node is less than search key then we keep on moving forward on the same level.
        2. Key of next node is greater than the key to be inserted then we store the pointer to current 
        node i at update[i] and move one level down and continue our search.

        At the lowest level (0), if the element next to the rightmost element (update[0]) has key equal 
        to the search key, then we have found key otherwise failure.

        The expected number of steps in each linked list is at most 1/p, which can be seen by tracing 
        the search path backwards from the target until reaching an element that appears in the next 
        higher list or reaching the beginning of the current list. Therefore, the total expected cost 
        of a search is 1/p(log_1/p(n)) which is O(log n) when p is a constant.

        Args:
            key: Data to search for in skip list
        
        Return:
            Boolean indicating whether key was found

        Raises:

        """
        # X (current)
        current = self.__header

        # Start from highest level of skip list move the current reference forward while node next 
        # to current's key is less than key. 
        for i in range(self.__MAX_LEVEL, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]

        # Reached level 0 and advance reference to right, which is possibly our desired node
        current = current.forward[0]

        # If current node have key equal to search key, we have found our target node
        if current and current.key == key:
            return True
        else:
            return False

    def erase(self, key):
        """
        Deletion of an element k is preceded by locating element in the Skip list using above 
        mentioned search algorithm. Once the element is located, rearrangement of pointers is done 
        to remove element from list just like we do in singly linked list. We start from lowest level 
        and do rearrangement until element next to update[i] is not k.After deletion of element there 
        could be levels with no elements, so we will remove these levels as well by decrementing the 
        level of Skip list.

        Args:
            key: Data to remove from skip list

        Return:

        Raises:
            ValueError: Key not in skiplist
        """
        # Here update[i] holds the pointer to node at level i from which we moved down 
        # to level i-1 and pointer of node left to deletion position at level 0.
        update = [None] * (self.__MAX_LEVEL + 1)

        # X (current)
        current = self.__header

        # Start from highest level of skip list move the current reference forward while node next 
        # to current's key is less than key. Otherwise insert current in update and move one level 
        # down and continue search
        for i in range(self.__MAX_LEVEL, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        # Reached level 0 and forward reference to right is desired position to delete key.
        current = current.forward[0]

        # If current node is target node
        if current and current.key == key:
            # start from lowest level and rearrange references just like we do in singly linked list
            # to remove target node
            for i in range(self.__level + 1):
                # If at level i, next node is not target node, break the loop, no need to move 
                # to a further level
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]
            # Remove levels having no elements
            while(self.__level > 0 and self.__header.forward[self.__level] == None):
                self.__level -= 1

        elif current and current.key != key:
            raise ValueError('Key not in skip list')

    def __str__(self):
        """
        Return string representation of skip list
        """
        stringrep, header = '\n*****Skip List******\n', self.__header
        for level in range(self.__level + 1, -1, -1):
            stringrep += "Level {}: ".format(level)
            node = header.forward[level]
            while(node != None):
                stringrep += '{} '.format(node.key)
                node = node.forward[level]
            stringrep += "\n"
        return stringrep

    class SkipNode:
        """
        Inner class representing nodes in skiplist

        We speak of a Skip List node having levels, one level per 
        forward reference. The number of levels in a node is called 
        the size of the node.

        Attributes:
            key: Data stored in node
            forward: forward array carrying pointers to nodes of a different level. A level i node carries i forward pointers indexed through 0 to i.
        """
        def __init__(self, key, level):
            """
            Initialize SkipNode attributes with values

            Args:
                key: Data stored in SkipNode
                level: Level of the node is chosen randomly during insertion in the list. Level i being the topmost level and level 0 being the bottom level.
            """
            self.key = key
            self.forward = [None] * (level + 1)

myskiplist = SkipList()
myskiplist.insert(5)
myskiplist.insert(7)
myskiplist.insert(20)
myskiplist.insert(8)
print(myskiplist)
print(myskiplist.search(12))
myskiplist.erase(7)
print(myskiplist)