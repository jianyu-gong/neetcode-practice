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

        curr = head

        OldToNew = {None: None}

        while curr:
            OldToNew[curr] = Node(curr.val)
            curr = curr.next

        
        curr = head

        while curr:
            copy = OldToNew[curr]
            copy.next = OldToNew[curr.next]
            copy.random = OldToNew[curr.random]
            curr = curr.next

        return OldToNew[head]