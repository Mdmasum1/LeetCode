'''
Leet code 965: Univalued Binary Tree:

A binary tree is uni-valued if every node in the tree has the same value.

Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.


'''

from typing import Optional  # import Optional for type hints (node can be None)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):  # constructor with default value 0 and no children
        self.val = val  # store the node's value
        self.left = left  # reference to left child (default None)
        self.right = right  # reference to right child (default None)


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:  # entry point, takes root node
        return self._isUnivalTree(root, root.val)  # start recursion, using root's value as the target value

    def _isUnivalTree(self, node: Optional[TreeNode], val: int) -> bool:  # helper: checks node and its subtree against val
        if not node:  # base case: empty node (None)
            return True  # vacuously true, nothing to violate the condition
        if node.val != val:  # current node's value differs from target value
            return False  # tree is not univalued
        return self._isUnivalTree(node.left, val) and self._isUnivalTree(node.right, val)  # recurse into both children

    # T:O(n); S:O(n)  # time O(n): visits every node once; space O(n): recursion stack depth


if __name__ == "__main__":
    # Test case 1
    # Input: root = [1,1,1,1,1,None,1]
    # Output: true
    root1 = TreeNode(1)
    root1.left = TreeNode(1)
    root1.right = TreeNode(1)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(1)
    root1.right.right = TreeNode(1)

    solution = Solution()
    ret1 = solution.isUnivalTree(root1)
    print(ret1)  # True

    # Test case 2
    # Input: root = [2,2,2,5,2]
    # Output: false
    root2 = TreeNode(2)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.left = TreeNode(5)
    root2.left.right = TreeNode(2)

    ret2 = solution.isUnivalTree(root2)
    print(ret2)  # False