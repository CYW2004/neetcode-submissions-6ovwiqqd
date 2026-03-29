class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        step = [float('inf')] * n
        step[0] = 0

        def dfs(i):
            for j in range(i):
                if step[j] == float('inf'):
                    dfs(j)
                if j + nums[j] >= i:
                    step[i] = min(step[i], step[j] + 1)
            return step[i]

        return dfs(n - 1)