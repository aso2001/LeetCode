# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        ## Recursive with slicing
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder.pop(0))
        pos = inorder.index(root.val)
        root.left = self.buildTree(preorder, inorder[:pos])
        root.right = self.buildTree(preorder, inorder[pos + 1:])
        return root

    def buildTree2(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Recursive without slicing
        def dfs(idx, start, end):
            if start > end:
                return None
            root = TreeNode(preorder[idx])
            pos = inorder.index(preorder[idx])
            root.left = dfs(idx + 1, start, pos - 1)
            root.right = dfs(idx + pos - start + 1, pos + 1, end)
            return root

        return dfs(0, 0, len(preorder) - 1)