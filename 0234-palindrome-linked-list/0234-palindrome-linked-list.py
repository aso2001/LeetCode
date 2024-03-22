# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur = head
        res = []
        while cur:
            res.append(cur.val)
            cur = cur.next
        for i in range(len(res)//2):
            if res[i] != res[len(res) - i - 1]:
                return False
        return True

    def isPalindrome2(self, head: Optional[ListNode]) -> bool:
        # Find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Inverse 2nd half of the list: 1->2->2->1  =>  1->2->2<-1
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        # Check left and right side of the list if polindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True