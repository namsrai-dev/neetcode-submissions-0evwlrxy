# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(tree1, tree2, depth=0):
            indent = "  " * depth
            t1_val = tree1.val if tree1 else "None"
            t2_val = tree2.val if tree2 else "None"
            
            print(f"{indent}DFS Level {depth}: Comparing Node({t1_val}) vs Node({t2_val})")
            
            if tree1 and tree2:
                if tree1.val != tree2.val:
                    print(f"{indent}!! Value Mismatch: {tree1.val} != {tree2.val}")
                    return False
                
                # Checking Left
                print(f"{indent}Checking Left of {tree1.val}...")
                if tree1.left and tree2.left:
                    if not dfs(tree1.left, tree2.left, depth + 1):
                        return False
                elif tree1.left or tree2.left:
                    print(f"{indent}!! Left Structure Mismatch: One is None, one is not.")
                    return False

                # Checking Right
                print(f"{indent}Checking Right of {tree1.val}...")
                if tree1.right and tree2.right:
                    if not dfs(tree1.right, tree2.right, depth + 1):
                        return False
                elif tree1.right or tree2.right:
                    print(f"{indent}!! Right Structure Mismatch: One is None, one is not.")
                    return False
                
                print(f"{indent}Result for Node({tree1.val}): MATCH")

            elif tree1 or tree2:
                print(f"{indent}!! Structure Mismatch: One tree ended early.")
                return False
            
            return True

        return dfs(p, q)