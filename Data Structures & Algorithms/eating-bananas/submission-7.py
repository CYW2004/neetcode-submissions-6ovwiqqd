class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)

        if n == h:
            return max(piles)

        l, r = 1, max(piles)

        while l != r:
            mid = (l + r) // 2
            time = 0
            for i in range(n):
                time += math.ceil(piles[i] / mid)
            if time > h:
                l = mid + 1
            else:
                r = mid
        
        return l