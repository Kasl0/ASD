class BSTNode:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

def find(root, key):
    while root != None:
        if root.key == key:
            return root
        elif key < root.key:
            root = root.left
        else:
            root = root.right
    return None

def insert(root, val):
    if not root:
        return BSTNode(val)
    prev = None
    p = root
    while p is not None:
        if val > p.val:
            prev = p
            p = p.right
        elif val < p.val:
            prev = p
            p = p.left
        else:
            return root
    if prev.val < val:
        prev.right = BSTNode(val)
    else:
        prev.left = BSTNode(val)
    return root

def BSTmin(root):
    if root == None:
        return None
    while root.left != None:
        root = root. left
    return root

def BSTnext(node):
    if node.right is not None:
        return BSTmin(node.right)
    while node.parent.right == node:
        node = node.parent
    return node.parent