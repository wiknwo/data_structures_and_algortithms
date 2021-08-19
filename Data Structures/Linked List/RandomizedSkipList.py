from random import randrange
class RandomizedSkipList:
    """
    Class representing randomized skiplist.

    Towers: The columns of SkipNodes are known as towers. 
    Towers are linked together by the down reference in the 
    SkipNode.

    Levels: Each Horizontal Group of SkipNodes Is a Level.
    If you look closely, you will notice that each level is 
    actually an ordered linked list of SkipNodes where the 
    order is maintained by the key.

    Attributes:

    Methods:
        flip(): Returns 1 or 0 denoting heads or tails respectively
    """
    def __init__(self):
        """
        Initialize attributes of randomized skip list
        """
        self.__header = self.SkipNode()
        self.__trailer = self.SkipNode()
        self.__header.next = self.__trailer
        self.__trailer.previous = self.__header

    def flip(self):
        """
        Performs coin toss giving heads or tails with
        probability 0.5
        """
        return randrange(2)

    def search(self, key):
        """
        Returns true if the key exists in the SkipList 
        or false otherwise.
        """
        current = self.__header

        # Traverse skiplist
        while current:
            if current.next.key == None:
                current = current.down
            else:
                if current.next.key == key:
                    return True
                else:
                    # If the key we are looking for is 
                    # less than the key contained in the SkipNode
                    # we know that no other SkipNode on 
                    # that level can contain our key since everything 
                    # to the right has to be greater. In that case, we 
                    # drop down one level in that tower. 
                    if key < current.next.key:
                        current = current.down
                    
                    # On the other hand, as long as there are 
                    # SkipNodes on the current level with key 
                    # values less than the key we are looking for, 
                    # we continue moving to the next node
                    else:
                        current = current.next
                        
        # If no such level exists (we drop to None), 
        # we have discovered that the key is not present 
        # in our skip list. We break out of the loop 
        # and return False. 
        return False

    def insert(self, key):
        """
        Insert the key into the skip list
        """
        # Check to see if this is first node being added to skiplist
        if self.__header.next == self.__trailer:
            print('First node being inserted')
            tmp = self.SkipNode(key)
            self.__header.next = tmp
            tmp.previous = self.__header
            tmp.next = self.__trailer
            self.__trailer.previous = tmp
            top = tmp
            # If we are adding to the head of the list, 
            # a new SkipNode must be created and the
            # head's next pointer should point to it.
            # The iteration in lines continues 
            # as long as the flip method returns a 1 (the 
            # coin toss returns heads). Each time a new 
            # level is added to the tower, a new SkipNode 
            # and a new header are created.
            while self.flip() == 1:
                newhead = self.SkipNode()
                tmp = self.SkipNode(key)
                tmp.down = top
                top.up = tmp
                newhead.next = tmp
                tmp.previous = newhead
                newtail = self.SkipNode()
                newtail.previous = tmp
                tmp.next = newtail
                newtail.down = self.__trailer
                self.__trailer.up = newtail
                self.__trailer = newtail
                newhead.down = self.__header
                self.__header.up = newhead
                self.__header = newhead
                top = tmp
        # In the case of a non-empty skip list 
        # we need to search for the insert position 
        # as described above. Since we have no way of 
        # knowing how many SkipNodes will be added 
        # to the tower, we need to save the insert points 
        # for every level that we enter as part of the 
        # search process. 
        else:
            tower = [] # Stack to hold tentative insert points  
            current = self.__header

            while current:
                if current.next.key is None:
                    tower.append(current)
                    current = current.down
                else:
                    if current.next.key > key:
                        tower.append(current)
                        current = current.down
                    else:
                        current = current.next
            lowest_level = tower.pop()
            tmp = self.SkipNode(key)
            tmp.next = lowest_level.next
            lowest_level.next.previous = tmp
            lowest_level.next = tmp
            tmp.previous = lowest_level
            top = tmp

            while self.flip() == 1:
                if not tower: # Check if stack is empty
                    newhead = self.SkipNode()
                    tmp = self.SkipNode(key)
                    tmp.down = top
                    top.up = tmp
                    newhead.next = tmp
                    tmp.previous = newhead
                    newtail = self.SkipNode()
                    newtail.previous = tmp
                    tmp.next = newtail
                    newtail.down = self.__trailer
                    self.__trailer.up = newtail
                    self.__trailer = newtail
                    newhead.down = self.__header
                    self.__header.up = newhead
                    self.__header = newhead
                    top = tmp
                else:
                    next_level = tower.pop()
                    tmp = self.SkipNode(key)
                    tmp.down = top
                    top.up = tmp
                    tmp.next = next_level.next
                    next_level.next.previous = tmp
                    next_level.next = tmp
                    tmp.previous = next_level
                    top = tmp

    def erase(self, key):
        """
        Erases key from skiplist
        """
        current = self.__header
        
        # Traverse skiplist
        while current:
            if current.next.key == None:
                current = current.down
            else:
                if current.next.key == key:
                    # delete current.next
                    current = current.next
                    while current.down != None:
                        current = current.down
                    while current.up != None:
                        tmp = current
                        predecessor = current.previous
                        successor = current.next
                        predecessor.next = successor
                        successor.previous = predecessor
                        current = tmp.up
                    return True
                else:
                    if key < current.next.key:
                        current = current.down
                    else:
                        current = current.next
        return False 

    def __str__(self):
        """
        Return string representation of skip list
        """
        stringrep, current, level = '\n*****Skip List*****\n', self.__header, self.__header
        while level != None:
            while current.next.key != None:
                stringrep += '{} '.format(current.next.key)
                current = current.next
            stringrep += '{} \n'.format(current.key)
            level = level.down
            current = level
        return stringrep
        
    class SkipNode:
        """
        Inner class represting nodes in skip list

        Attributes:
            key: Data to be stored in SkipNode
            up: Pointer to SkipNode above this node
            down: Pointer to SkipNode below this node
            previous: Pointer to SkipNode before this node
            next: Pointer to SkipNode after this node

        Methods:
        """
        def __init__(self, key = None, up = None, down = None, previous = None, next = None):
            """
            Initializes node's attributes with values
            """
            self.key = key
            self.up = up
            self.down = down
            self.previous = previous
            self.next = next

myskiplist = RandomizedSkipList()
# myskiplist.insert(2)
# myskiplist.insert(3)
# myskiplist.insert(4)
# myskiplist.insert(7)
print(myskiplist)