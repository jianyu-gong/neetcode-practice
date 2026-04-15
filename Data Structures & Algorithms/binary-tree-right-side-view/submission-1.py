# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []

        # def dfs(node, depth):
        #     if not node:
        #         return

        #     if depth == len(res):
        #         res.append(node.val)

        #     dfs(node.right, depth + 1)
        #     dfs(node.left, depth + 1)

        # dfs(root, 0)

        # return res

        queue = deque([root])

        while queue:

            right_side = None
            queue_length = len(queue)

            for i in range(queue_length):
                node = queue.popleft()

                if node:
                    right_side = node
                    queue.append(node.left)
                    queue.append(node.right)

            if right_side:
                res.append(right_side.val)

        return res