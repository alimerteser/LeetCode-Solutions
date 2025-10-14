# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
        #LCA: The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself)

        if not root:
            return None

        if root.val > max(p.val, q.val): #If root value is greater than p value and q value, then LCA is at the left subtree
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < min(p.val, q.val): #If root value is less than p value and q value, then LCA is at the right subtree
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root