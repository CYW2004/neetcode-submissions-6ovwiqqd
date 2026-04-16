class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = {}
        def dp(n):
            if n == 0:
                return 0
            elif n < 0:
                return float("inf")
            elif n not in mem:
                mem[n] = min(dp(n - c) + 1 for c in coins)
            return mem[n]

        res = dp(amount)
        return -1 if res == float("inf") else res