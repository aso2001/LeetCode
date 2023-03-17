# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Solution using custom heapq __lt__ function
        setattr(ListNode, "__lt__", lambda self, other: self.val <= other.val)

        dummy = ListNode()
        tail = dummy

        hh = []
        for l in lists:
            if l:
                heapq.heappush(hh, l)

        while hh:
            cur = heapq.heappop(hh)
            tail.next = cur
            tail = tail.next
            if cur and cur.next:
                heapq.heappush(hh, cur.next)
        return dummy.next