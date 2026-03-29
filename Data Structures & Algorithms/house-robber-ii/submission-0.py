class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 4:
            return max(nums)

        cur_max = nums[0]   # ok to jump from
        new_sum = nums[1]   # cannot immediately use
        
        for i in range(2, n - 1):
            tmp = cur_max
            cur_max = max(cur_max, new_sum) 
            new_sum = tmp + nums[i]

        max1 = max(cur_max, new_sum)

        cur_max = nums[-1]   # ok to jump from
        new_sum = nums[0]   # cannot immediately use
        
        for i in range(1, n - 2):
            tmp = cur_max
            cur_max = max(cur_max, new_sum) 
            new_sum = tmp + nums[i]

        max2 = max(cur_max, new_sum)

        return max(max1, max2)