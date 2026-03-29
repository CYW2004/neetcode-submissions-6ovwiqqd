class Solution:
    def isHappy(self, n: int) -> bool:
        if n % 1 != 0:
            return False

        seen = set()

        def check(n):
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)
            
            sum = 0
            while n != 0:
                r = n % 10
                sum += r * r
                n = n // 10
            
            return check(sum)

        return check(n)
            