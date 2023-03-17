# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        def middle(head):
            prev = ListNode(0)
            prev.next = head
            slow, fast = head, head
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            prev.next = None
            left = head
            right = slow
            return (left, right)

        def dfs(head):
            (left, right) = middle(head)
            if not left:
                return None
            if left == right:
                root = TreeNode(left.val)
                return root
            root = TreeNode(right.val)
            root.left = dfs(left)
            root.right = dfs(right.next)
            return root
        
        return dfs(head)