class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        def dp(index):
            if index == 0:
                return nums[0]
            local_max = float("-inf")
            prod = 1
            for i in range(index, -1, -1):
                cur = nums[i]
                prod *= cur
                local_max = max(prod, local_max)
            return max(local_max, dp(index - 1))

        return dp(n - 1)