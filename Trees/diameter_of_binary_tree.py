from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #Given the root of a binary tree, return the length of the diameter of the tree.
        #The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
        #The length of a path between two nodes is represented by the number of edges between them.

        #We use Depth First Search (DFS) algorithm.

        d = 0 #We use a global variable so that we can update maximum diameter.

        def dfs(root: Optional[TreeNode]):
            if root is None: return 0

            nonlocal d

            left_height = dfs(root.left)
            right_height = dfs(root.right)
            d = max(d, left_height + right_height)

            return 1 + max(left_height, right_height)

        dfs(root)

        return d
