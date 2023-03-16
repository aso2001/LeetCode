# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def inOrder(root):
            nonlocal ss
            if not root:
                return
            inOrder(root.right)
            tmp = root.val
            root.val += ss
            ss += tmp
            inOrder(root.left)

        ss = 0
        inOrder(root)
        return root 

    
    def convertBST2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def inOrder(root):
            nonlocal ss
            if not root:
                return
            inOrder(root.left)
            ss += root.val
            inOrder(root.right)

        def inOrderBig(root):
            nonlocal tmp
            if not root:
                return
            inOrderBig(root.left)
            tmp += root.val
            root.val += ss - tmp
            inOrderBig(root.right)

        ss = 0
        inOrder(root)
        tmp = 0
        inOrderBig(root)
        return root 