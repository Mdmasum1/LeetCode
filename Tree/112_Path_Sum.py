'''
P: Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that 
adding up all the values along the path equals targetSum.
A leaf is a node with no children.

Ex 1: Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22    
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

Ex 2:
Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.
 
'''

from typing import List, Optional

#Every tree has common class TreeNode
class TreeNode:

    #Default constructor
    def __init__(self, val=0, left=None, right=None):
        self.val= val
        self.left= left
        self.right = right

class Solution:

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        #Base case
        if root is None:
            return False

        #Initialize stack with root node and its value root.val  
        stack = [(root, root.val)]

        while stack:
            node, curSum = stack.pop()

            if node.left is None and node.right is None and curSum == targetSum:
                return True

            #From this point looking for root's child
            if node.left:
                stack.append((node.left, node.left.val + curSum))
            if node.right:
                stack.append((node.right, node.right.val + curSum))

        return False

#T:O(n); S:O(N) ; complexity for the wrost case scenario.

# Quick manual test
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)

sol = Solution()
print(sol.hasPathSum(root, 22))  # Expected: True
print(sol.hasPathSum(root, 99))  # Expected: False
print(sol.hasPathSum(None, 99))  # Expected: False



