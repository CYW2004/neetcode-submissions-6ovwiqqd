# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(root):
            if not root.left:
                lmin = root.val
            else:
                bool1, lmax, lmin = check(root.left)
                if not bool1 or lmax >= root.val:
                    return (False, 0, 0)

            if not root.right:
                rmax = root.val
            else:
                bool2, rmax, rmin = check(root.right)
                if not bool2 or rmin <= root.val:
                    return (False, 0, 0)

            return (True, rmax, lmin)

        return check(root)[0]

            