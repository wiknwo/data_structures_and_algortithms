from collections import deque

class TreeNode:
    """Class representing standard binary tree node

    Attributes:
        left(TreeNode): Reference to left child of tree node
        right(TreeNode): Reference to right child of tree node
        data: Store data associated with node

    Methods:
        print_in_order_traversal(): Prints the nodes in the binary tree in order
        print_pre_order_traversal(): Prints the nodes in the binary tree (root, left, right)
        print_post_order_traversal(): Prints the nodes in the binary tree (left, right, root)
        max_width_of_binary_tree(root): Returns the maximum width of the binary tree
        height(root): Returns the height of the binary tree
        dfs(root): Returns iterative depth-first traversal of binary tree
        recursive_dfs(root): Returns recursive depth-first search of binary tree
        bfs(root): Returns breadth-first traversal of binary tree O(n)
        contains(root, target): Checks whether tree contains the target iteratively
        recursive_contains(root, target): Checks whether tree contains target recursively
        is_leaf(): Checks whether the current node is a leaf/external node 
        is_internal(): Checks whether the current node is an internal node
        dfs_min_value_in_binary_tree(root): Calculates the minimum number in the binary tree through depth-first search
        bfs_min_value_in_binary_tree(root): Calculates the minimum number in the binary tree through breadth-first search
        recursive_min_value_in_binary_tree(root): Caluclates the minimum number in the binary tree recursively
        dfs_max_value_in_binary_tree(root): Calculates the maximum number in the binary tree through depth-first search
        bfs_max_value_in_binary_tree(root): Calculates the maximum number in the binary tree through breadth-first search
        recursive_max_value_in_binary_tree(root): Caluclates the maximum number in the binary tree recursively
        max_path_sum(root): Calculate the maxmimum path sum from the root to a leaf node
        check_bst(root): Returns boolean determining if the binary tree is a binary search tree
    """
    def __init__(self, data):
        """Initializes tree node by setting references to left and right and assigning data"""
        self.left = None
        self.right = None
        self.data = data    

    def print_in_order_traversal(self):
        """Method to print in order traversal of binary tree (left, root, right)"""
        if self.left is not None:
            self.left.print_in_order_traversal()

        print(self.data)

        if self.right is not None:
            self.right.print_in_order_traversal()
    
    def print_pre_order_traversal(self):
        """Method to print pre order traversal of binary tree (root, left, right)"""
        print(self.data)

        if self.left is not None:
            self.left.print_pre_order_traversal()

        if self.right is not None:
            self.right.print_pre_order_traversal()

    def print_post_order_traversal(self):
        """Method to print post order traversal of binary tree (left, right, root)"""

        if self.left is not None:
            self.left.print_pre_order_traversal()

        if self.right is not None:
            self.right.print_pre_order_traversal()

        print(self.data)

    def max_width_of_binary_tree(self, root):
        """
        Returns maximum width of given binary tree. The maximum width among all levels.
        The width of one level is defined as the length between the end-nodes (The leftmost
        and rightmost non-null nodes in the level, where the null nodes between the end-nodes)
        are also counted into the calculation.
        """
        q, width = deque([(root, 0)]), 0 # Create deque keeping track of node and index number
        while q:
            left_most_node, left_most_index = q[0]
            right_most_node, right_most_index = q[-1]
            width = max(width, right_most_index - left_most_index + 1)
            q_next_level = deque()
            while q:
                node, index = q.popleft()
                if node.left:
                    q_next_level.append((node.left, index * 2 + 1))
                if node.right:
                    q_next_level.append((node.right, index * 2 + 2))
            q = q_next_level
        return width    

    def height(self, root):
        """Method to compute height of binary tree"""
        # base case
        if root is None:
            return -1

        # Inductive step
        return max(self.height(root.left), self.height(root.right)) + 1

    def sum_values_in_binary_tree(self, root):
        """Method to return the sum of values in the binary tree"""
        # Base case
        if root is None:
            return 0

        # Inductive step
        return root.data + self.sum_values_in_binary_tree(root.left) + self.sum_values_in_binary_tree(root.right)

    def iterative_sum_values_in_binary_tree(self, root):
        """Method to return the sum of values in the binary tree iteratively"""
        if root == None: 
            return 0
        total_sum, q = 0, [root]
        while q:
            current_node = q.pop(0)
            total_sum += current_node.data
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
        return total_sum

    def dfs(self, root):
        """Method to perform a depth-first traversal of the binary tree"""
        if root is None:
            return []
        result, stack = [], [root]
        while stack:
            current_node = stack.pop()
            result.append(current_node.data)
            # Performing the step which decides order in 
            # which tree is traversed. If we push the 
            # right child then the left child we will get
            # the left child at the top of the stack on the
            # next iteration and vice versa.
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
        return result

    def recursive_dfs(self, root):
        """Method to perform a recursive depth-first search of the binary tree"""
        # Base case
        if root is None:
            return []
        
        # Inductive step
        left_binary_tree = self.recursive_dfs(root.left)
        right_binary_tree = self.recursive_dfs(root.right)
        return [root.data] + left_binary_tree + right_binary_tree

    def bfs(self, root):
        """Method to perform breadth-first traversal of binary tree"""
        if root is None:
            return []
        result, queue = [], [root]
        while queue:
            current_node = queue.pop(0)
            result.append(current_node.data)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return result
        
    def contains(self, root, target):
        """Method to check if tree contains the target data"""
        if root is None: 
            return False
        queue = [root]
        while queue:
            current_node = queue.pop(0)
            if current_node.data == target:
                return True
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return False
    
    def recursive_contains(self, root, target):
        """Method to check if tree contains target recursively"""
        # Base case
        if root is None:
            return False
        if root.data == target:
            return True
        
        # Inductive step
        return self.recursive_contains(root.left, target) or self.recursive_contains(root.right, target)

    def is_leaf(self):
        """Method to check is current node in tree is a leaf/external node"""
        if self is None:
            return False
        if self.left is None and self.right is None:
            return True
        return False

    def is_internal(self):
        """Method to check if current node in tree is an internal node"""
        if self is None:
            return False
        if self.left is not None or self.right is not None:
            return True
        return False

    def dfs_min_value_in_binary_tree(self, root):
        """Method to return the minimum value in the binary tree"""
        if root is None:
            return float('inf')
        minimum_value, stack = float('inf'), [root]
        while stack:
            current_node = stack.pop()
            minimum_value = min(minimum_value, current_node.data)

            if current_node.right is not None:
                stack.append(current_node.right)
            if current_node.left is not None:
                stack.append(current_node.left)
        return minimum_value

    def bfs_min_value_in_binary_tree(self, root):
        """Method to return the minimum value in the binary tree"""
        if root is None:
            return float('inf')
        minimum_value, queue = float('inf'), [root]
        while queue:
            current_node = queue.pop(0)
            minimum_value = min(minimum_value, current_node.data)

            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return minimum_value
    
    def recursive_min_value_in_binary_tree(self, root):
        """Method to compute the minimum value in the binary tree recursively"""
        # Base case
        if root is None:
            return float('inf')

        # Inductive step
        min_left_tree = self.recursive_min_value_in_binary_tree(root.left)
        min_right_tree = self.recursive_min_value_in_binary_tree(root.right)
        return root.data if root.data < min_left_tree and root.data < min_right_tree else min(min_left_tree, min_right_tree)

    def dfs_max_value_in_binary_tree(self, root):
        """Method to return the maximum value in the binary tree"""
        if root is None:
            return float('-inf')
        maximum_value, stack = float('-inf'), [root]
        while stack:
            current_node = stack.pop()
            maximum_value = max(maximum_value, current_node.data)

            if current_node.right is not None:
                stack.append(current_node.right)
            if current_node.left is not None:
                stack.append(current_node.left)
        return maximum_value

    def bfs_max_value_in_binary_tree(self, root):
        """Method to return the maximum value in the binary tree through bfs"""
        if root is None:
            return float('-inf')
        maximum_value, q = float('-inf'), [root]
        while q:
            current_node = q.pop(0)
            maximum_value = max(maximum_value, current_node.data)

            if current_node.left is not None:
                q.append(current_node.left)
            if current_node.right is not None:
                q.append(current_node.right)
        return maximum_value
    
    def recursive_max_value_in_binary_tree(self, root):
        """Method to compute the maximum value in the binary tree recursively"""
        # Base case
        if root is None:
            return float('-inf')
        
        # Inductive step
        max_left_tree = self.recursive_max_value_in_binary_tree(root.left)
        max_right_tree = self.recursive_max_value_in_binary_tree(root.right)
        return root.data if root.data > max_left_tree and root.data > max_right_tree else max(max_left_tree, max_right_tree)

    def max_path_sum(self, root):
        """Method to compute the max path sum in the binary tree from the root to a leaf node"""
        # Base cases
        if root is None:
            return float('-inf')
        if root.is_leaf():
            return root.data
        
        # Inductive step
        max_path_sum_left_tree = root.max_path_sum(root.left)
        max_path_sum_right_tree = root.max_path_sum(root.right)
        return max(root.data, root.data + max(max_path_sum_left_tree, max_path_sum_right_tree))

    def check_bst(self, root):
        """
        Method to check if given binary tree is a valid binary search tree.

        All values in subtree left of root must be strictly less than the root
        All values in subtree right of root must be strictly greater than the root
        All subtrees must also be binary search trees
        """
        return self.__check_bst_helper(root, float('-inf'), float('inf'))

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

root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
print("max_width_of_binary_tree(): {}".format(root.max_width_of_binary_tree(root)))
print("**In Order Traversal**")
root.print_in_order_traversal()
print("**Pre Order Traversal**")
root.print_pre_order_traversal()
print("**Post Order Traversal**")
root.print_post_order_traversal()
print("Height of binary tree: {}".format(root.height(root)))
print("Sum of values in binary tree: {}".format(root.sum_values_in_binary_tree(root)))
print("Depth-First Traversal of binary tree: {}".format(root.dfs(root)))
print("Recursive Depth-First Traversal of binary tree: {}".format(root.recursive_dfs(root)))
print("Breadth-First Traversal of binary tree: {}".format(root.bfs(root)))
print("Check if tree contains target ({0}): {1}".format(3, root.contains(root, 3)))
print("Check if tree contains target ({0}): {1}".format(100, root.contains(root, 100)))
print("Check if tree contains target ({0}): {1}".format(100, root.recursive_contains(root, 100)))
print("Check if tree contains target ({0}): {1}".format(3, root.contains(root, 3)))
print("is_leaf(): {}".format(root.left.left.is_leaf()))
print("is_internal(): {}".format(root.left.left.is_internal()))
print("is_internal(): {}".format(root.is_internal()))
print("Sum of values in binary tree (iterative): {}".format(root.iterative_sum_values_in_binary_tree(root)))
print("Minimum value in binary tree (dfs): {}".format(root.dfs_min_value_in_binary_tree(root)))
print("Minimum value in binary tree (bfs): {}".format(root.bfs_min_value_in_binary_tree(root)))
print("Minimum value in binary tree (recursive): {}".format(root.recursive_min_value_in_binary_tree(root)))
print("Maximum value in binary tree (dfs): {}".format(root.dfs_max_value_in_binary_tree(root)))
print("Maximum value in binary tree (bfs): {}".format(root.bfs_max_value_in_binary_tree(root)))
print("Maximum value in binary tree (recursive): {}".format(root.recursive_max_value_in_binary_tree(root)))
print("Maximum path sum from root to leaf: {}".format(root.max_path_sum(root)))
print("Check if binary tree is binary search tree: {}".format(root.check_bst(root)))