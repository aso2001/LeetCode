# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative solution
        res = []
        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res

    
    def inorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        # Recursive solution
        res = []
        def inOrder(root, res):
            if not root:
                return res
            inOrder(root.left, res)
            res.append(root.val)
            inOrder(root.right, res)
        
        inOrder(root, res)
        return res