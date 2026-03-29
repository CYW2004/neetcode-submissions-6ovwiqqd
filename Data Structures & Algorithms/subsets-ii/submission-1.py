class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        maxIndex = len(nums) - 1
        
        # prev is the previous unselected number
        def dfs(index, cur_res, prev):
            if index > maxIndex:
                res.append(cur_res.copy())
                return
                
            num = nums[index]
            if num == prev:
                dfs(index + 1, cur_res.copy(), prev)
            else:
                dfs(index + 1, cur_res.copy(), num)    # num not selected
                cur_res.append(num)
                dfs(index + 1, cur_res, prev)   # num selected

        dfs(0, [], None)
        return res