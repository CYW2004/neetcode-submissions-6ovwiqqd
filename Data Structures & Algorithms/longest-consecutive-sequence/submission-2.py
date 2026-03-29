class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        
        res = 1
        d = defaultdict(int)

        for num in nums: 
            d[num] = 1

        for num in nums:
            if d[num - 1] == 0 and d[num + 1] == 1:
                cnt = 1
                while d[num + 1] == 1:
                    cnt += 1
                    num += 1
                res = max(res, cnt)

        return res