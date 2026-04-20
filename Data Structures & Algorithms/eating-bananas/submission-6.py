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
                if piles[i] % mid == 0:
                    time += piles[i] // mid
                else:
                    time += (piles[i] // mid) + 1
            if time > h:
                l = mid + 1
            else:
                r = mid
        
        return l