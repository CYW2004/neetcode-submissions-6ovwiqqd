class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):
            res = digits[i] + 1
            if res == 10 and i == 0:
                digits[i] = 0
                digits.insert(0, 1)
                break
            elif res == 10:
                digits[i] = 0
                continue
            else:
                digits[i] = res
                break

        return digits