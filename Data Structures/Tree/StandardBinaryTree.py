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
        max_width_of_binary_tree(): Returns the maximum width of the binary tree
        height(): Returns the height of the binary tree
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