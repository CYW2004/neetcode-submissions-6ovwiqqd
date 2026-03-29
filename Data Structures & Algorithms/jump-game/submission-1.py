class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        def dfs(i):
            if i == length - 1:
                return True
            n = nums[i]
            if n == 0:
                return False
            else:
                end = min(length - 1, i + n)
                for j in range(i + 1, end + 1):
                    if dfs(j):
                        return True
                return False
        
        return dfs(0)