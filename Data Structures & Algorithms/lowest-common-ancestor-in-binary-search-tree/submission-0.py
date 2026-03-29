# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        rt = root
        if p.val < q.val:
            small, large = p, q
        else:
            small, large = q, p

        while True:
            if rt.val < small.val:
                rt = rt.right
            elif rt.val > large.val:
                rt = rt.left
            else:
                break

        return rt