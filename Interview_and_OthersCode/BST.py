
''' Problem: Find BST successor   (with prampt)

 Intuition and definantion: The sunccessor of a node in a Binary Search Tree(BST)
  is the node with the smallest key greater than the key of the given node .
  Here's I find the successor of a given node in a BST:

   1. If node has a right subtree:
     ---> The successor is the minumum value in the right subtree

    2. If the node does not have a right subtree:

     ---> Move up using the parent reference until you find a node
      that is the left child of its parent. The parent of that 
      node will be the successor.


'''
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.parent = None
        self.key = key

def find_min(node):
    while node.left is not None:
        node = node.left
    return node

def find_successor(node):
    # Case 1: Node has a right subtree
    if node.right:
        return find_min(node.right)
    
    # Case 2: Node does not have a right subtree
    successor = None
    ancestor = node.parent
    while ancestor and node == ancestor.right:
        node = ancestor
        ancestor = ancestor.parent
    successor = ancestor
    
    return successor

# Example usage:
# Construct the BST
root = TreeNode(20)
root.left = TreeNode(10)
root.left.parent = root
root.right = TreeNode(30)
root.right.parent = root
root.left.left = TreeNode(5)
root.left.left.parent = root.left
root.left.right = TreeNode(15)
root.left.right.parent = root.left

node = root.left  # Node with key 10
successor = find_successor(node)
if successor:
    print("Successor of node with key", node.key, "is node with key", successor.key)
else:
    print("Node with key", node.key, "has no successor")










