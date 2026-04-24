# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:


        fast = slow = head

        for _ in range(n):
            fast = fast.next

        if not fast:
            return None

        while fast:
            pre = slow
            fast = fast.next
            slow = slow.next
        
        pre.next = slow.next

        return head