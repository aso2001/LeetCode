"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
    
        if not root: return None
        q, lev = deque(), deque()
        q.append(root)

        while q:
            nxt = None
            while q:
                cur = q.popleft()
                cur.next = nxt
                nxt = cur
                if cur.right:
                    lev.append(cur.right)
                if cur.left:
                    lev.append(cur.left)
            q = lev.copy()
            lev = deque()
        return root