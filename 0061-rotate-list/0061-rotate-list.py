# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def length(head):
            cnt = 0
            while head:
                cnt += 1
                head = head.next
            return cnt
        
        def split(head, k):
            cnt = 0
            while cnt < k - 1:
                cnt += 1
                head = head.next
            nxt = head.next
            head.next = None
            return nxt

        llen = length(head)
        if llen > 0 and k > llen: k %= llen
        if not head or not k or llen == 1 or k == llen: return head
        nxt = split(head, llen - k)
        cur, prev = nxt, nxt
        while cur:
            prev = cur
            cur = cur.next
        prev.next = head
        return nxt