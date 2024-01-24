# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def preOrder(root, dd):
            if not root:
                return 0
            dd[root.val] += 1
            if not root.left and not root.right:
                cnt = 0
                for d in dd:
                    if dd[d] % 2:
                        if cnt:
                            return 0
                        else:
                            cnt = 1
                return 1
            left = preOrder(root.left, dd.copy())
            right = preOrder(root.right, dd.copy())
            return left + right
        
        dd = defaultdict(int)
        return preOrder(root, dd)