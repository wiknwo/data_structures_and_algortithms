class PerfectSkipList:
    """
    Class representing perfect skip lists in python

    Think of a skip list like a sorted linked list with shortcuts (wormholes?)
    How did we form this special linked list? 
    - We started with a normal linked list (level 0)
    - Then we took every other node in level 0 (2nd node from original list) and added them to level 1
    - Then we took every other node in level 1 (4th node from the original list) and raised it to level 2
    - Then we took every other node in level 2 (8th node from the original list) and raised it to level 3
    - Then we took every other node in level i (2^ith node from the original list) and raised it to level i + 1
    - There will be ceil(O(log2(n)) levels where n is the number of keys in the skiplist

    Attributes:

    Methods:
        search(key): 
        erase(key):
        insert(key):
        rebalance():
    """
    def __init__(self, max_level = 16):
        """
        Initializes attributes of SkipList with values
        """
        # Maximum level for this skip list
        self.__MAX_LEVEL = max_level

        # Create header node and initialize to -1
        self.__header = self.SkipNode(-1, self.__MAX_LEVEL)

        # Current level of skip list
        self.__level = 0

        # Number of keys in skiplist
        self.__size = 0
    
    def __rebalance(self):
        """
        Maintains perfect structure of skip list that ensures O(log(n)) performance
        """
        print('*******Rebalancing*******')
        # X (current), j (index representing position of SkipNode in bottom-most level), previous
        current, j, = self.__header, 1

        # Go through all level 0 nodes and elevate every 2^ith node to level i 
        # wit i ranging from 1 <= i <= MAX_LEVEL
        while current.forward[0]:
            for i in range(self.__MAX_LEVEL, -1, -1):
                if j % 2**i == 0: 
                    print('j = {} | i = {} | 2**i = {} | current.forward[0].key = {} | current.forward[0].size = {}'.format(j, i, 2**i, current.forward[0].key, current.forward[0].size))
                    if current.forward[0].size == i + 1:
                        break
                    elif current.forward[0].size != i + 1:
                        new_node = self.SkipNode(current.forward[0].key, i)
                        print('new_node.size = {}'.format(new_node.size))
                        print(new_node.forward)
                        for k in range(len(current.forward)):
                            new_node.forward[k] = current.forward[k].forward[0]
                            current.forward[k] = new_node
                        
            current = current.forward[0]
            j += 1
        print(self.__size)

    def search(self, key):
        """
        How long would it take us to find an item or determine it is not present in the list? O(log(n))

        Proof:

        - At each level we visit at most 2 nodes: At any node, x, in level i, you sit between two nodes 
        (p,q) at level i+1 and you will need to visit at most one other node in level i before descending
        VISUALIZATION HELPS http://ee.usc.edu/~redekopp/cs104/slides/L23_SkipLists.pdf

        - There are O(log(n)) levels

        - So we visit at most O(2*log(n)) levels = O(log(n))
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
        return True if current and current.key == key else False       
    
    def erase(self, key):
        """
        Deletion of an element k is preceded by locating element in the Skip list using above 
        mentioned search algorithm. Once the element is located, rearrangement of pointers is done 
        to remove element from list just like we do in singly linked list. We start from lowest level 
        and do rearrangement until element next to update[i] is not k.After deletion of element there 
        could be levels with no elements, so we will remove these levels as well by decrementing the 
        level of Skip list. Then we have to REBALANCE the perfect skip list.

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

        # Rebalance perfect skip list
        self.__rebalance()

    def insert(self, key):
        """
        We will start from highest level in the list and compare key of 
        next node of the current node with the key to be inserted. Basic idea is:

        1. Key of next node of current node is less than key to be inserted 
        then we keep on moving forward on the same level

        2. Key of next node of current node is greater than the key to be inserted 
        then we store the pointer to current node i at update[i] and move one level 
        down and continue our search.

        3. Rebalance perfect skip list

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
            
            # Create new SkipNode with level 0
            new_node = self.SkipNode(key, 0)

            # Insert node by rearranging pointer references
            for i in range(new_node.size):
                new_node.forward[i] = update[i].forward[i]
                update[i].forward[i] = new_node

            # Increment size of skip list
            self.__size += 1

            # Rebalance perfect skip list
            self.__rebalance()

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
        Inner class representing nodes in perfect skiplist

        We speak of a Skip List node having levels, one level per 
        forward reference. The number of levels in a node is called 
        the size of the node.

        Attributes:
            key: Data stored in node
            forward: forward array carrying pointers to nodes of a different level. A level i node carries i forward pointers indexed through 0 to i.
            size: Number of levels in node
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
            self.size = len(self.forward)

myperfectskiplist = PerfectSkipList()
myperfectskiplist.insert(5)
myperfectskiplist.insert(7)
myperfectskiplist.insert(2)
myperfectskiplist.insert(9)
print(myperfectskiplist)