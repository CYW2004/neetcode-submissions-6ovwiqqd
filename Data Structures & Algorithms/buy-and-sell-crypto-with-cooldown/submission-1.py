class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        mem = {}
        mem[(0, 0)] = float("-inf")
        ans = 0

        def dp(i, isBuy):
            nonlocal ans

            if (i, isBuy) in mem:
                return mem[(i, isBuy)]

            if isBuy == 1:
                res = max([0] + [dp(j, 0) for j in range(i - 1)]) - prices[i]
                mem[(i, isBuy)] = res
                return res
            else:
                res = max([dp(j, 1) for j in range(i)]) + prices[i]
                mem[(i, isBuy)] = res
                ans = max(res, ans)
                return res

        for i in range(n):
            dp(i, 1)
            dp(i, 0)

        return ans