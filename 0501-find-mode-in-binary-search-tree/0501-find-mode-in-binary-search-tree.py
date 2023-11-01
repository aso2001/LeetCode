# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root):
            if root:
                res.append(root.val)
                dd[root.val] += 1
                dfs(root.left)
                dfs(root.right)
            return
            
        dd, res = defaultdict(int), []
        dfs(root)
        mx = max(dd.values())
        return [key for key in dd if dd[key] == mx]