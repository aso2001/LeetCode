# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        
    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        ## Recursive solution without helper function
        if not root:
            return 0
        depthL = self.maxDepth(root.left)
        depthR = self.maxDepth(root.right)
        return 1 + max(depthL, depthR)

        # Recursive solution with helper
        def Depth(root):
            if not root:
                return 0
            depthL = Depth(root.left)
            depthR = Depth(root.right)
            return 1 + max(depthL, depthR)
        
        return Depth(root)

    
def maxDepth3(self, root: Optional[TreeNode]) -> int:
        ## Iterative BFS solution
        q = collections.deque()
        q.append(root)
        depth = 0
        while q:
            llev = len(q)
            for _ in range(llev):
                cur = q.popleft()
                if cur:
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
                else: return 0
            depth += 1
        return depth

    
def maxDepth4(self, root: Optional[TreeNode]) -> int:
        ## Iterative DFS solution

        stack = []
        stack.append([root, 1])
        maxdepth = 0

        while stack:
            cur, depth = stack.pop()
            if cur:
                maxdepth = max(maxdepth, depth)
                if cur.left:
                    stack.append([cur.left, depth + 1])
                if cur.right:
                    stack.append([cur.right, depth + 1])
            else:
                return 0
        return maxdepth
            
