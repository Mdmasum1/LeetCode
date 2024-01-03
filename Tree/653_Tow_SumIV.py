
''' 653--Two Sum IV - Input is a BST
--Given the root of a binary search tree and an integer k, 
--return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.

'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: [TreeNode], k: int) -> bool:
        hashSet = set()
        return self.helper(root, k, hashSet)
    
    def helper(self, node, k, hashSet):
        if node is None: # Base case
            return False
        
        if k - node.val in hashSet:
            return True
        
        hashSet.add(node.val)
        return self.helper(node.left, k, hashSet) or self.helper(node.right, k, hashSet)

# Function to insert nodes into the tree
def insertLevelOrder(arr, root, i, n):
    if i < n:
        temp = TreeNode(arr[i])
        root = temp

        root.left = insertLevelOrder(arr, root.left, 2 * i + 1, n)
        root.right = insertLevelOrder(arr, root.right, 2 * i + 2, n)
    return root

# Given list representation of the tree
arr = [5, 3, 6, 2, 4, None, 7]
n = len(arr)
root = None
root = insertLevelOrder(arr, root, 0, n)

# Check for k = 9
k = 9
sol = Solution()
result = sol.findTarget(root, k)
print(result)


