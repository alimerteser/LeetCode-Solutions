from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #Invert the binary tree and return its node
        #left = 1, right = 5 -> left = 5, right = 1
        #left = 2, right = None -> left = None, right = 2
        #left = None, right = 3 -> left = 3, right = None

        if root is None: #if the tree is null, then there is no need to continue
            return None

        if root.left or root.right:
            tmp = root.left
            root.left = root.right
            root.right = tmp
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)

        return root
