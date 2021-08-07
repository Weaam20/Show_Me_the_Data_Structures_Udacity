class Node(object):
    def __init__(self, data, frequency=0, right=None, left=None):
        self.data = data
        self.frequency = frequency
        self.right = right
        self.left = left
        self.huff = ''

    def has_right(self):
        return self.right is not None

    def has_left(self):
        return self.left is not None

    def is_leaf(self):
        return self.left is None and self.right is None

