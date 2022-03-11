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
        if root is None:
            return []
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
        if root is None:
            return False
        if root.data == target:
            return True
        return self.recursive_contains(root.left, target) or self.recursive_contains(root.right, target)

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
