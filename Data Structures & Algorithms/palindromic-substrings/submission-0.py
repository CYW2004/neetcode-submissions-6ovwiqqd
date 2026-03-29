class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)

        for i in range(n):
            for j in range (n - 1, i - 1, -1):
                if s[i] == s[j]:
                    front, back = i, j
                    while front <= back and s[front] == s[back]:
                        front += 1
                        back -= 1
                    if front >= back:       # valid palindrome
                        res += 1

        return res