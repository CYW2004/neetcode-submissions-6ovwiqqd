class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(index, cur_res, cur_sum):
            prev = None
            for i in range(index, len(candidates)):
                num = candidates[i]
                if num == prev:
                    continue
                prev = num
                
                new_sum = cur_sum + num
                if new_sum > target:
                    break
                elif new_sum == target:
                    cur_res.append(num)
                    res.append(cur_res.copy())
                else:
                    cur_res.append(num)
                    dfs(i + 1, cur_res, new_sum)
                
                cur_res.pop()
        
        dfs(0, [], 0)
        return res
