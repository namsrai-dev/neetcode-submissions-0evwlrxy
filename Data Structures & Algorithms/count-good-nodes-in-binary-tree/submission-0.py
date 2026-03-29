# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, max_num):
            count = 0

            if not root:
                return 0

            if root.val >= max_num:
                count+=1
                max_num = root.val

            if root.left:
                count += dfs(root.left, max_num)
            if root.right:
                count += dfs(root.right, max_num)

            return count
            

        return dfs(root, root.val)