class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_cnt = 0
        for num in nums:
            if num == 0:
                zero_cnt += 1
            else:
                prod *= num
        
        if zero_cnt > 1:
            return [0] * len(nums)
        
        res = []
        for num in nums:
            if zero_cnt == 0:
                res.append(prod // num)
            else:
                if num == 0:
                    res.append(prod)
                else:
                    res.append(0)
        
        return res