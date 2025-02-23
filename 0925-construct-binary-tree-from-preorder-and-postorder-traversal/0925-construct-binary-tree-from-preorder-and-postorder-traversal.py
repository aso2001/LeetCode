# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        d = defaultdict()
        for i in range(len(preorder)):
            d[preorder[i]] = i

        def helper(L, R, postorder):
            if R == L:
                return None

            if R - L == 1:
                return TreeNode(postorder.pop())

            root = TreeNode(postorder.pop())
            idx = d[postorder[-1]]
            
            root.right=helper(idx, R, postorder)
            root.left=helper(L + 1, idx, postorder)
            return root

        return helper(0, len(preorder), postorder)