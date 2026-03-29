# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 1]
            
            left = dfs(root.left)
            right = dfs(root.right)

            if not left[0] or not right[0]:
                return [False, 0]

            if left[1] - right[1] > 1 or right[1] - left[1] > 1:
                return [False, 0]

            return [True, 1 + max(left[1], right[1])]

        return dfs(root)[0]


