"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head: return None
        dd = {}
        cur = head
        while cur:
            new = Node(cur.val)
            dd[cur] = new
            cur = cur.next

        cur = head
        while cur:
            rnd = cur.random
            if cur.next:
                dd[cur].next = dd[cur.next]
            else:
                dd[cur].next = None
            if rnd:
                dd[cur].random = dd[rnd]
            else:
                dd[cur].random = None
            cur = cur.next
        return dd[head]