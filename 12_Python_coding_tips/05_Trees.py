# Tree are recursive data structures (like linked lists)
# Binary Search Tree (BST)
class TreeNode(object):
    """A tree with two children trees"""

    def __init__(self
                 data, parent=None, left=None, right=None):

        self.data = data
        self.parent = parent
        self.left = left
        self.right = right
        # Search (BST)

    def search(self, value):
        if self.data is None:
            return None

        




