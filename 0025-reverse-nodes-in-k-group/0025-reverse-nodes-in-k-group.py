# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prevs = None # pointer to head of subgroup of k elements
        prev = None # pointer to head of reversed final list
        tail = head # pointer to tail of final list
        curr = head
        if curr.next is None:
            return head
    
        flag = 0 # flag = 0 controls first subgroup of k elements. flag = 1 controls linkage of other subgroups to previous group
        count = 0
        while True:
            while count < k and curr: # reverse k elements in subgroup
                tmp = curr.next
                curr.next = prevs
                prevs = curr
                curr = tmp
                count += 1
            if count < k: # last group of elements, reverse again if group is shorter than k
                prevl = None # pointer to head of last short subgroup
                while prevs:
                    tmp = prevs.next
                    prevs.next = prevl
                    prevl = prevs 
                    prevs = tmp
                tail.next = prevl # link tail of final list to last short subgroup
            count = 0
            if curr:
                if flag == 0:
                    flag = 1
                    prev = prevs
                    tail = prevs
                    while tail.next:
                        tail = tail.next # move tail pointer to the end of linked subgroup
                else:
                    tail.next = prevs
                    while tail.next:
                        tail = tail.next
                prevs = None
            else:
                if flag == 0:
                    flag == 1
                    prev = prevs
                    tail = prevs
                    while tail.next:
                        tail = tail.next # move tail pointer to the end of linked subgroup
                if prevs and flag == 1:
                    tail.next = prevs # link last subgroup
                break
        return prev