# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def countNodes(maxv, node):
            if not node:
                return 0

            if node.val >= maxv:
                maxv = node.val
                return 1 + countNodes(maxv, node.left) + countNodes(maxv, node.right)
            else:
                return countNodes(maxv, node.left) + countNodes(maxv, node.right)
        
        return countNodes(root.val, root)
