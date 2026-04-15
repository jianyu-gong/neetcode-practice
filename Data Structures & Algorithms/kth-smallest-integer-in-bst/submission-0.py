# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse(self, root, num_list):
        if not root:
            return

        self.traverse(root.left, num_list)
        num_list.append(root.val)
        self.traverse(root.right, num_list)






    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        num_list = []

        self.traverse(root, num_list)
        print(num_list)

        return num_list[k-1]



        