# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cur = head
        cnt = 0
        while cur:
            cur = cur.next
            cnt += 1
        quotient, remainder = divmod(cnt, k)
        cur = head
        res = []
        for i in range(k):
            tmp = cur
            for j in range(quotient + (i < remainder) - 1):
                if cur:
                    cur = cur.next
            if cur:
                x = cur.next
                cur.next = None
                cur = x
            res.append(tmp)
        return res   