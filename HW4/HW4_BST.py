class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class BST:
    """Binary search tree"""

    def __init__(self):
        self.root = None

    def search(self, value):
        """Return the node with the given value"""
        node = self.root

        while node and value != node.value:
            if value < node.value:
                node = node.left
            else:
                node = node.right
        if node:
            return node
        else:
            raise Exception('The given value cannot be found.')

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            self.root.parent = None
            return
        self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if not node.left:
                node.left = Node(value)
                node.left.parent = node
            else:
                self._insert(node.left, value)
        else:
            if not node.right:
                node.right = Node(value)
                node.right.parent = node
            else:
                self._insert(node.right, value)

    def _height(self, node):
        if node == None:
            return -1
        return max(self._height(node.left), self._height(node.right)) + 1

    def height(self):
        return self._height(self.root)

    def tree_minimum(self, node=None):
        """Return a reference to the node with the minimum value in the tree"""
        if node is None:
            node = self.root
        current = node
        while current:
            if not current.left:
                break
            current = current.left
        return current

    def tree_maximum(self, node=None):
        """Return a reference to the node with the maximum value in the tree"""
        if node is None:
            node = self.root
        current = node
        while current:
            if not current.right:
                break
            current = current.right
        return current

    def successor(self, x):
        """returns the successor of node x in the sorted order of the nodes
        as determined by an inorder tree walk"""
        x = self.search(x)
        if x.right:
            return self.tree_minimum(x.right)

        y = x.parent
        while y and x == y.right:
            x = y
            y = y.parent
        return y



