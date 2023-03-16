# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        res = []
        dd = defaultdict(list)

        def preOrder(root):
            if not root:
                return 'null'
            s = ','.join([str(root.val), preOrder(root.left), preOrder(root.right)])
            if len(dd[s]) == 1:
                res.append(root)
            dd[s].append(root)
            return s

        preOrder(root)
        return res