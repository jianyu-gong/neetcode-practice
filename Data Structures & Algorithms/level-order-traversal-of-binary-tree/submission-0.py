# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = [root]
        res = []

        while queue:

            temp_list = []
            queue_length = len(queue)
            # print(queue_length)

            for _ in range(queue_length):
                root_poped = queue.pop(0)
                temp_list.append(root_poped.val)
                if root_poped.left:
                    queue.append(root_poped.left)
                
                if root_poped.right:
                    queue.append(root_poped.right)
            
            res.append(temp_list)

        return res
