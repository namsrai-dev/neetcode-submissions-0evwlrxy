# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        my_queue = [[root]]
        ret = []

        while my_queue:
            popped = my_queue.pop(0)
            my_arr = []
            my_arr2 = []
            for new_root in popped:
                my_arr2.append(new_root.val)
                if new_root.left:
                    my_arr.append(new_root.left)
                if new_root.right:
                    my_arr.append(new_root.right)
            
            ret.append(my_arr2)
            if len(my_arr) > 0:
                my_queue.append(my_arr)


        return ret