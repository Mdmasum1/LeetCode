'''
Problem:

'''
# Definition for a binary tree node.


from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self._invertTree(root)

        #Finally, return the original root of the tree
        return root


    def _invertTree(self, root: Optional) -> Optional[TreeNode]:
        #Base case
        if root is None:
            return 
        
        #Swap between left and right
        root.left, root.right = root.right, root.left

        #Recursive case
        self._invertTree(root.left)
        self._invertTree(root.right)

#TO(n), S:O(n)

if __name__ == "__main__":
    # Test case 1
    # Input: root = [4,2,7,1,3,6,9]
    # Output: [4,7,2,9,6,3,1]
    root1 = TreeNode(4)
    root1.left = TreeNode(2)
    root1.right = TreeNode(7)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(3)
    root1.right.left = TreeNode(6)
    root1.right.right = TreeNode(9)

    solution = Solution()
    ret1 = solution.invertTree(root1)
    print(ret1.val, ret1.left.val, ret1.right.val,
          ret1.left.left.val, ret1.left.right.val,
          ret1.right.left.val, ret1.right.right.val)
    # Expected: 4 7 2 9 6 3 1

    # Test case 2
    # Input: root = []
    # Output: []
    root2 = None

    ret2 = solution.invertTree(root2)
    print(ret2)  # None
        