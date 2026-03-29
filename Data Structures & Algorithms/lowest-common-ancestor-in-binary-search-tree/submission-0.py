# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        min_val = min(p.val,q.val)
        max_val = max(p.val,q.val)

        if root.val <= max_val and root.val >= min_val:
            return root

        elif root.val > max_val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < min_val:
            return self.lowestCommonAncestor(root.right, p, q)
