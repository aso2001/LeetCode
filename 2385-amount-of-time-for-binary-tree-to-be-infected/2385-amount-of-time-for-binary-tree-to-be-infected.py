# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def tree_to_graph(root):
            nonlocal dd, prev
            if not root:
                return           
            if prev != root.val:           
                if prev in dd:
                    dd[prev].append(root.val)
                else:
                    dd[prev] = [root.val]
                dd[root.val] = [prev]
                prev = root.val
            tree_to_graph(root.left)
            prev = root.val
            tree_to_graph(root.right)
            return dd

        dd = {}
        prev = root.val
        tree_to_graph(root)

        q = deque([start])
        visited = set()
        res = 0
        nxt = deque()
        while True:
            while q:
                cur = q.pop()
                visited.add(cur)
                if cur in dd:
                    for nei in dd[cur]:
                        if nei not in visited:
                            nxt.append(nei)
            if nxt:
                q = nxt.copy()
                nxt = deque()
            else:
                return res
            res += 1