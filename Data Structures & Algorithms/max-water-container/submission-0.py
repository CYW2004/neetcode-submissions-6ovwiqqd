class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            h_left = heights[l]
            h_right = heights[r]
            amt = min(h_left, h_right) * (r - l)
            if amt > res:
                res = amt
            if h_left > h_right:
                r -= 1
            else:
                l += 1

        return res