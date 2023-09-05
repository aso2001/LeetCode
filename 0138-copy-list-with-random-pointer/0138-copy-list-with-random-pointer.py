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
        new = Node(cur.val)
        res = new
        dd[cur] = new
        cur = cur.next
        prev = new
        while cur:
            new = Node(cur.val)
            dd[cur] = new
            prev.next = new
            prev = new
            cur = cur.next

        cur = head
        new = res
        while cur:
            rnd = cur.random
            if rnd:
                new.random = dd[rnd]
            cur = cur.next
            new = new.next
        return res