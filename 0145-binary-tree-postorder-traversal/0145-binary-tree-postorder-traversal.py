# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def _postorder_traversal_helper(self, current_node, result):
        if not current_node:
            return
        self._postorder_traversal_helper(current_node.left, result)
        self._postorder_traversal_helper(current_node.right, result)
        result.append(current_node.val)

    def postorderTraversal(self, root):
        result = []
        self._postorder_traversal_helper(root, result)
        return result