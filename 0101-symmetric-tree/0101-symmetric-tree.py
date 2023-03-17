# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Recursive solution
        def dfs(L, R):
            if L and R:
                return L.val == R.val and dfs(L.left, R.right) and dfs(L.right, R.left)
            return L == R

        return dfs(root.left, root.right)

    
    def isSymmetric2(self, root: Optional[TreeNode]) -> bool:
        # Iterative solution
        if root is None: return True
        
        les, res = [], []
        les.append(root)
        res.append(root)

        while len(res) > 0:
            lcur = les.pop()
            rcur = res.pop()

            if lcur.val != rcur.val:
                return False
            if lcur.left:
                if rcur.right:
                    les.append(lcur.left)
                    res.append(rcur.right)
                else:
                    return False
            else:
                if rcur.right:
                    return False
            if lcur.right:
                if rcur.left:
                    les.append(lcur.right)
                    res.append(rcur.left)
                else:
                    return False
            else:
                if rcur.left:
                    return False
        return True