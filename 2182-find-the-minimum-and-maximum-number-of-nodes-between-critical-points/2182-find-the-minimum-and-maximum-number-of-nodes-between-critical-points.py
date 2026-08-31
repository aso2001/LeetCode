# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        res = [-1, -1]
        min_dist = math.inf
        prev = head
        cur = head.next
        cur_idx = 1
        prev_cri_idx = 0
        first_cri_idx = 0
        while cur.next is not None:
            if (cur.val < prev.val and cur.val < cur.next.val) or (cur.val > prev.val and cur.val > cur.next.val):
                if prev_cri_idx == 0:
                    prev_cri_idx = cur_idx
                    first_cri_idx = cur_idx
                else:
                    min_dist = min(min_dist, cur_idx - prev_cri_idx)
                    prev_cri_idx = cur_idx
            cur_idx += 1
            prev = cur
            cur = cur.next
        if min_dist != math.inf:
            max_dist = prev_cri_idx - first_cri_idx
            res = [min_dist, max_dist]
        return res