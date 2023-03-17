# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        ## Optimized Recursive with slicing

        idx = {}
        for i in range(len(inorder)):
            idx[inorder[i]] = i

        def helper(L, R):
            if L > R:
                return None
            root = TreeNode(postorder.pop())
            pos = idx[root.val]
            root.right = helper(pos + 1, R)
            root.left = helper(L, pos - 1) 
            return root

        return helper(0, len(inorder) - 1)

    def buildTree2(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        ## Recursive with slicing
        if not postorder or not inorder:
            return None
        root = TreeNode(postorder.pop())
        pos = inorder.index(root.val)
        root.left = self.buildTree(inorder[:pos], postorder)
        root.right = self.buildTree(inorder[pos + 1:], postorder)
        return root