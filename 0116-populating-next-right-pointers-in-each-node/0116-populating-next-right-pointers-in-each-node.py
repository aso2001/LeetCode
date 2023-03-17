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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        # Iterative BFS
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
                    level.append(cur) #.val)  # change to pointer to node from val
                else:
                    return None
            #print(level)
            nxt = None
            for i in range(len(level) - 1, -1, -1):
                level[i].next = nxt
                nxt = level[i]
        return root