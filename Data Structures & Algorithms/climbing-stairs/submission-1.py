class Solution:
    def climbStairs(self, n: int) -> int:
        cur = 1
        prev = 1

        for i in range (0, n - 1, 1):
            temp = cur
            cur = cur + prev
            prev = temp

        return cur
