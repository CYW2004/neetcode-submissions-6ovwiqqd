class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        l = 0

        for l in range(0, len(nums) - 2):
            r = len(nums) - 1
            while l < r - 1:
                target = 0 - nums[l] - nums[r]
                for i in range(l + 1, r):
                    if nums[i] == target:
                        sol = sorted([nums[l], nums[i], nums[r]])
                        if res == []:
                            res.append(sol)
                        else:
                            for arr in res:
                                if arr == sol:
                                    res.remove(sol)
                                    break
                            res.append(sol)
                            
                r -= 1

        return res

                    