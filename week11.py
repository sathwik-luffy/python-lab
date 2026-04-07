class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    """Helper function to insert a new node into the BST."""
    if root is None:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def preorder(root):
    """Root -> Left -> Right"""
    if root:
        print(root.val, end=" ")
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    """Left -> Root -> Right (Sorted Order)"""
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

def postorder(root):
    """Left -> Right -> Root"""
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=" ")

# dont write this code 👇👇👇👇 until mam says ok for this,but write in your rough
root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.left.left = Node(3)
root.left.right = Node(7)


print("Pre-order Traversal:")
preorder(root)

print("\nIn-order Traversal:")
inorder(root)

print("\nPost-order Traversal:")
postorder(root)