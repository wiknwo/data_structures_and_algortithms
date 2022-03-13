class TreeNode:
    """
    Class representing binary search tree node. 

    Attributes:
        data(): Data stored in node
        left(TreeNode): Pointer to left child
        right(TreeNode): Pointer to right child
    """
    def __init__(self, data):
        """Initializes node with data and pointers to left and right children"""
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    """
    A Binary Search Tree is a Binary Tree that satisfies the 
    following properties:

    1. Each internal node holds a (unique) value.

    2. A **total-order relation (~) is defined on those values.
        a. Reflexive: k ~ k
        b. Antisymmetric: if k1 ~ k2 and k2 ~ k1 then k1 = k2
        c. Transitive: if k1 ~ k2 and k2 ~ k3 then k1 ~ k3
    
    - All the values (k_i) in the left sub-tree of a node with value k satisfy the relation k_i ~ k.
    - All the values (k_j) in the right sub-tree of a node with value k satisfy the relation k ~ k_j.

    The properties can also be stated like this:

    1. The left subtree of a node contains only nodes with keys lesser than the node’s key.
    2. The right subtree of a node contains only nodes with keys greater than the node’s key.
    3. The left and right subtree each must also be a binary search tree.

    Attributes: 
        root(TreeNode): The root of the binary search tree
        size(int): Number of nodes in BST

    Methods:
        insert(data): Inserts node with given data into BST while maintaining order property
        size(): Returns the number of nodes in the BST
        is_empty(): Returns boolean indicating if BST is empty
        contains_iterative(data): Returns boolean indicating if data is contained in BST
        contains(data): Returns boolean indicating if data is contained in BST recursively
        remove(data): Returns boolean indicating if data was sucessfully removed from BST
        print_in_order_traversal(): Prints the BST in order which happens to be sorted in ascending order
        check_bst(): Checks if binary tree is a BST
    """
    def __init__(self):
        """Initializes Binary Search Tree with root"""
        self.__root = None

    def insert(self, data):
        """Method to insert node into binary search tree"""
        if self.__root is None:
            self.__root = TreeNode(data)
        else:
            self.__insert(data, self.__root)

    def __insert(self, data, current_node):
        """Helper method to insert a new node with given data into binary search tree"""
        if data <= current_node.data:
            if current_node.left is None:
                current_node.left = TreeNode(data)
            else:
                self.__insert(data, current_node.left)
        else:
            if current_node.right is None:
                current_node.right = TreeNode(data)
            else:
                self.__insert(data, current_node.right)

    def size(self):
        """Method to count number of nodes in binary search tree"""
        return self.__size(self.__root)

    def __size(self, node):
        """Helper method to count number of nodes in BST"""
        if node == None:
            return 0
        else:
            return 1 + self.__size(node.left) + self.__size(node.right)

    def is_empty(self):
        """Method to check if binary search tree is empty"""
        return self.__root == None
    
    def contains_iterative(self, data):
        """Method to check if binary search tree contains value"""
        current_node = self.__root
        while current_node is not None:
            if data == current_node.data:
                return True
            if data < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False

    def contains(self, data):
        """Method to check if BST contains data point recursively"""
        if self.is_empty():
            raise ValueError('BST is empty!')
        else:
            return self.__contains(data, self.__root)

    def __contains(self, data, current_node):
        """Helper method to check if binary search tree contains value"""
        if data == current_node.data:
            return True
        elif data < current_node.data:
            if current_node.left is None:
                return False
            else:
                return self.__contains(data, current_node.left)
        else:
            if current_node.right is None:
                return False
            else:
                return self.__contains(data, current_node.right)
    
    def remove(self, key):
        """Method to remove node with given key from BST if it exists"""
        if self.is_empty():
            raise ValueError('BST is empty!')
        else:
            self.__hibbard_deletion(self.__root, key)

    def __hibbard_deletion(self, root, key):
        """
        Method to remove node containing data from binary search tree
        There are four cases to cover:

        1. Deleting a node with no children
        2. Deleting a node with a left child
        3. Deleting a node with a right child
        4. Deleting a node with two children

        By the way, I'd like to point out that this deletion algorithm 
        is not suitable for balanced trees since it will not preserve the 
        balance. This algorithm is called Hibbard deletion, and one company 
        was sued in the past for implementing
        https://www.youtube.com/watch?v=gcULXE7ViZw
        """
        if root is None:
            # The root is none
            return None
        if key > root.data:
            # right sutree
            root.right = self.__hibbard_deletion(root.right, key)
        elif key < root.data:
            # left subtree
            root.left = self.__hibbard_deletion(root.left, key)
        else:
            if not (root.left or root.right):
                # Node to be deleted has no children so replace with None
                root = None
            elif root.right:
                # Replace current node with successor
                root.data = self.__successor(root)
                root.right = self.__hibbard_deletion(root.right, root.data)
            else:
                # Replace current node with predecessor
                root.data = self.__predecessor(root)
                root.left = self.__hibbard_deletion(root.left, root.data)
        return root
    
    def __successor(self, root):
        """
        Helper method to perform hibbard deletion.
        
        The successor to a key is the next largest key in 
        the tree and is conveniently found as the minimum 
        key in the right subtree of the node to be deleted.
        """
        root = root.right
        while root.left:
            root = root.left
        return root.data
        
    def __predecessor(self, root):
        """
        Helper method to perform hibbard deletion.

        The predecessor to a key is the next smallese key in 
        the tree and is conveniently found as the maximum 
        key in the left subtree of the node to be deleted.
        """
        root = root.left
        while root.right:
            root = root.right
        return root.data

    def print_in_order_traversal(self):
        """Method to print in order traversal of binary tree (left, root, right)"""
        print("***BST in order traversal***")
        self.__print_in_order_helper(self.__root)
    
    def __print_in_order_helper(self, node):
        """Helper method to print all nodes in BST in order"""
        if node.left is not None:
            self.__print_in_order_helper(node.left)

        print(node.data)

        if node.right is not None:
            self.__print_in_order_helper(node.right)

    def check_bst(self):
        """
        Method to check if given binary tree is a valid binary search tree.

        All values in subtree left of root must be strictly less than the root
        All values in subtree right of root must be strictly greater than the root
        All subtrees must also be binary search trees
        """
        return self.__check_bst_helper(self.__root, float('-inf'), float('inf'))

    def __check_bst_helper(self, root, min_value, max_value):
        """
        Helper method to check if tree is a binary search tree.
        """
        # Base case / stopping condition
        if root is None:
            return True
        # Base case / stopping condition and inductive step: Do some work to shrink the problem space
        elif self.__check_bst_helper(root.left, min_value, root.data) and self.__check_bst_helper(root.right, root.data, max_value):
            return True
        else:
            return False

    def __str__(self):
        """Method to return string representation of BST"""
        if self.is_empty():
            return ''
        bststring, stack = '', [self.__root]
        while stack:
            current_node, left_child, right_child = stack.pop(), None, None
            if current_node.left:
                left_child = current_node.left.data
            if current_node.right:
                right_child = current_node.right.data
            bststring += "Parent: {} | Left child: {} | Right child: {}\n".format(current_node.data, left_child, right_child)
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
            left_child, right_child = None, None
        return bststring

mybst = BinarySearchTree()
mybst.insert(100)
mybst.insert(70)
mybst.insert(80)
mybst.insert(45)
mybst.insert(209)
print("Binary search tree contains {}: {}".format(100, mybst.contains(100)))
print("Binary search tree contains {}: {}".format(10, mybst.contains(10)))
print("Size of Binary search tree: {}".format(mybst.size()))
print(mybst)
mybst.remove(70)
print(mybst)
print("Size of Binary search tree: {}".format(mybst.size()))
print("This BST is empty: {}".format(mybst.is_empty()))
print("This BST maintains the ordering property: {}".format(mybst.check_bst()))