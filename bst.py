#binary search tree (BST)

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def insert(root,x):
    if root is None:
        return Node(x)
    if root.data<x:
        root.right=insert(root.right,x)
    else:
        root.left=insert(root.left,x)
    return root
    
def create():
    root=None
    while True:
        x=int(input("Enter data to create node (0 to stop):"))
        #x=5
        if x==0:
            break
        root=insert(root,x)
    return root

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

root=create()
inorder(root)