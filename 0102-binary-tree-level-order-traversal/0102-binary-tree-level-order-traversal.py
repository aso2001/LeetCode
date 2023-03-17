# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Recursive solution
        def preOrder(root, dist):
            if root:
                if dist >= len(res):
                    res.append([])
                #print(root.val, dist)
                res[dist].append(root.val)
                preOrder(root.left, dist + 1)
                preOrder(root.right, dist + 1)
        
        res = []
        preOrder(root, 0)
        return res

    
    def levelOrder2(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Iterative solution
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            level = []                # list of items at current level
            llevel = len(q)           # Fix part of que for current level (since will add more nodes for next level)
            for _ in range(llevel):   # iterate through level
                cur = q.popleft()
                if cur:
                    if cur.left:
                        q.append(cur.left)
                    if cur and cur.right:
                        q.append(cur.right)
                    level.append(cur.val)
                else:
                    return []
            res.append(level)
        return res