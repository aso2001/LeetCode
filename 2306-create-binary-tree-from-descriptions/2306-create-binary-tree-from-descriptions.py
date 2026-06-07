# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        def buildTree(root):
            tn = TreeNode(root)
            if root in dd:
                if dd[root][0] >= 0:
                    tn.left = buildTree(dd[root][0])
                if dd[root][1] >= 0:
                    tn.right = buildTree(dd[root][1])
            return tn

        dd = {}
        parent = set()
        for d in descriptions:
            parent.add(d[0])
        for d in descriptions:
            if d[1] in parent:
                parent.remove(d[1])
            if d[0] not in dd:
                dd[d[0]] = [-1, -1]
            if d[2]:
                dd[d[0]][0] = d[1]
            else:
                dd[d[0]][1] = d[1]

        root = list(parent)[0]
        return buildTree(root)