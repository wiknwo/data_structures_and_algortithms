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
    """Class representing a Trie
    
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
        """Depth-first traversal of the trie
        
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
        
    def query(self, x):
        """Given an input (a prefix), retrieve all words stored in
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
        
t = Trie()
t.insert('was')
t.insert('word')
t.insert('war')
t.insert('what')
t.insert('where')
print(t.query('wh'))
