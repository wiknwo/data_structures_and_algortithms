# Credit to Albert Au Yeng for the code for a Trie in python
# https://albertauyeung.github.io/2020/06/15/python-trie.html/

class TrieNode:
    """A node in the trie structure"""

    def __init__(self, char):
        # the character stored in this node
        self.char = char

        # whether this can be the end of a word
        self.is_end = False

        # a counter indicating how many times a word is inserted
        # (if this node's is_end is True)
        self.counter = 0

        # a dictionary of child nodes
        # keys are characters, values are nodes
        self.children = {}

class Trie:
    """
    Class representing a Trie
    
    Trie is a very useful data structure. It is 
    commonly used to represent a dictionary for 
    looking up words in a vocabulary. 

    For example, consider the task of implementing a 
    search bar with auto-completion or query 
    suggestion. When the user enters a query, the 
    search bar will automatically suggests common 
    queries starting with the characters input by 
    the user.

    Trie is a tree-like data structure made up of nodes. 
    Nodes can be used to store data. Each node may have 
    none, one or more children. When used to store a 
    vocabulary, each node is used to store a character, 
    and consequently each "branch" of the trie represents 
    a unique word. 

    Attributes:
        root: The root of the trie

    Methods:
        insert(word): Inserts a word into the trie
        dfs(node, prefix): Performs a depth-first traversal of the trie
        query(x): Given a prefix, return all words starting with that prefix
    """
    def __init__(self):
        """
        The trie has at least the root node.
        The root node does not store any character
        """
        self.root = TrieNode("")
    
    def insert(self, word):
        """Insert a word into the trie"""
        node = self.root
        
        # Loop through each character in the word
        # Check if there is no child containing the character, create a new child for the current node
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                # If a character is not found,
                # create a new node in the trie
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        
        # Mark the end of a word
        node.is_end = True

        # Increment the counter to indicate that we see this word once more
        node.counter += 1
        
    def dfs(self, node, prefix):
        """
        Depth-first traversal of the trie
        
        Args:
            - node: the node to start with
            - prefix: the current prefix, for tracing a
                word while traversing the trie
        """
        if node.is_end:
            # If a word is found then append it to our output list
            self.output.append((prefix + node.char, node.counter))
        
        for child in node.children.values():
            self.dfs(child, prefix + node.char)
        
    def search(self, word):
        """Method to return boolean indicating if word exists in trie"""
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return node.is_end

    def query(self, x):
        """
        Given an input (a prefix), retrieve all words stored in
        the trie with that prefix, sort the words by the number of 
        times they have been inserted
        """
        # Use a variable within the class to keep all possible outputs
        # As there can be more than one word with such prefix
        self.output = []
        node = self.root
        
        # Check if the prefix is in the trie
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                # cannot found the prefix, return empty list
                return []
        
        # Traverse the trie to get all candidates
        self.dfs(node, x[:-1])

        # Sort the results in reverse order and return
        return sorted(self.output, key=lambda x: x[1], reverse=True)

    def __str__(self):
        """Method to return string representation of all words in trie"""
        # Traverse the trie to get all candidates
        self.output = []
        self.dfs(self.root, "")
        return '\n'.join(pair[0] for pair in sorted(self.output, key = lambda pair: pair[0]))

    def delete(self, word):
        """
        Method to delete word from trie if it exists

        1. Find word if it exists
        2. If the node exists and it has children then 
        we can't delete it and set the is_word flag to False
        3. If the node has no children then we can delete it
        and check if we can delete the parent
        4. If the node has no children and its counter is 0
        then delete it and check if we can delete its parent
        """
        node, parent = self.root, None

        # Find word in trie if it exists
        for char in word:
            if char in node.children:
                parent = node
                node = parent.children[char]
            else:
                # If character not in trie then word 
                # does not exist and we return False 
                # as we did not delete anything
                return False
        # Decrement the counter for this word
        print("Word on this recurse: {}, {}".format(word, node.children))
        if node.is_end:
            node.counter -= 1
            if not node.children and node.counter == 0:
                print("No children and counter == 0: {}".format(word))
                node.is_end = False
                node = None
                del parent.children[word[-1]]
                self.delete(word[:-1])
        elif not node.children and not node.is_end:
            print("Node has no children and it is not a word")
            del parent.children[word[-1]]
            node = None
            self.delete(word[:-1])

            
t = Trie()
t.insert('was')
t.insert('word')
t.insert('war')
t.insert('what')
t.insert('where')
t.insert('where')
print(t.query('wh'))
print(t)
print(t.search('where'))
t.delete('where')
t.delete('where')
print(t.query('wh'))
print(t)
t.delete('what')
print(t)
t.insert('what')
t.insert('where')
t.insert('what')
print(t.query('wh'))
print(t)