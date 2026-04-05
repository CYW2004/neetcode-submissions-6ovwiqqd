class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float("-inf")

        for index in range(n):
            prod = 1
            local_max = float("-inf")
            for i in range(index, -1, -1):
                prod *= nums[i]
                local_max = max(local_max, prod)
            ans = max(ans, local_max)

        return ans