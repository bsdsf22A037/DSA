import random

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        return node.height if node else 0

    def balance(self, node):
        return self.height(node.left) - self.height(node.right) if node else 0

    def rotate_right(self, y):
        if not y or not y.left:
            return y
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        return x

    def rotate_left(self, x):
        if not x or not x.right:
            return x
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y

    def insert(self, node, key):
        if node is None:
            return TreeNode(key)
        if key < node.value:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        balance = self.balance(node)

        if balance > 1 and key < node.left.value:
            return self.rotate_right(node)
        if balance > 1 and key > node.left.value:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1 and key > node.right.value:
            return self.rotate_left(node)
        if balance < -1 and key < node.right.value:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        return node

    def insert_value(self, value):
        self.root = self.insert(self.root, value)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)

    def inorder_traversal(self):
        if self.root:
            self.inorder(self.root)

tree = AVLTree()
for _ in range(500):
    val = random.randint(10, 20)
    tree.insert_value(val)
print("\nIn Order:\t", end="")
tree.inorder_traversal()
