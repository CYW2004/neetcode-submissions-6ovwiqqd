class Solution:
    def rob(self, nums: List[int]) -> int:
        # Assume we rob from small index to big index only
        n = len(nums)
        if n < 3:
            return max(nums)

        cur_max = nums[0]   # ok to jump from
        new_sum = nums[1]   # cannot immediately use
        
        for i in range(2, n):
            tmp = cur_max
            cur_max = max(cur_max, new_sum) 
            new_sum = tmp + nums[i]

        return max(cur_max, new_sum)