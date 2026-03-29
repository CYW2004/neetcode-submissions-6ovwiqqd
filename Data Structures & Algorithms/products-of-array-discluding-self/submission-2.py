class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zerocount = 0
        for num in nums:
            prod *= num
            if num == 0:
                zerocount += 1

        res = []
        if zerocount > 1:
            for num in nums:
                res.append(0)
            return res
        elif zerocount == 0:
            for num in nums:
                res.append(prod // num)
            return res
        else:
            prod = 1
            for num in nums:
                if num != 0:
                    prod *= num
            for num in nums:
                if num != 0:
                    res.append(0)
                else:
                    res.append(prod)
            return res
