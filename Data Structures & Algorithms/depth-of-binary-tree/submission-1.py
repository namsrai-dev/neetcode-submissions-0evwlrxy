# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.max_depth = 0
        if root:
            self.goDepth(1, root)
        return self.max_depth

    def goDepth(self, n, root):
        if n > self.max_depth:
            self.max_depth = n
        if root.left:
            self.goDepth(n+1, root.left)
        if root.right:
            self.goDepth(n+1, root.right)

        # if root:
        #     goDepth(1, root)

        
        