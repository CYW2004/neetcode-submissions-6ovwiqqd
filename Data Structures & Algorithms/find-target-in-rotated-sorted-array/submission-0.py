class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r + 1) // 2  # round up to avoid getting stuck
            mid = nums[m]
            right = nums[r]

            if mid <= right:
                if target >= mid and target <= right:
                    l = m
                else:
                    r = m - 1
            else:
                if target <= right:
                    l = m
                else:
                    r = m

        if target == nums[l]:
            return l
        else:
            return -1