# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def nodeCount(node):
            if not node:
                return 0
            else:
                return 1 + nodeCount(node.left) + nodeCount(node.right)

        def findK(root, nodeAcc, k):
            leftNum = nodeCount(root.left)
            nodeAcc += leftNum + 1

            if nodeAcc == k:
                return root.val
            elif nodeAcc < k:
                return findK(root.right, nodeAcc, k)
            else:
                nodeAcc -= leftNum + 1
                return findK(root.left, nodeAcc, k)

        return findK(root, 0, k)