# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow, fast = head, head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        second = slow.next

        pre = slow.next = None

        print(head.val, second.val)

        while second:
            temp = second.next
            second.next = pre
            pre = second
            second = temp

        second = pre

        while second:
            temp1, temp2 = head.next, second.next
            head.next = second
            second.next = temp1
            head, second = temp1, temp2
        

        