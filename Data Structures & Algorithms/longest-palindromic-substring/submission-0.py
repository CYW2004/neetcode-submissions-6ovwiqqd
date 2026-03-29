class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        reslen = 0
        n = len(s)

        for i in range(n):
            for j in range (n - 1, i - 1, -1):
                if j - i + 1 <= reslen:     # check if there is longer palindrome
                    break

                if s[i] == s[j]:
                    front, back = i, j
                    while front <= back and s[front] == s[back]:
                        front += 1
                        back -= 1
                    if front >= back:       # valid palindrome
                        res = s[i:j + 1]
                        reslen = j - i + 1

        return res

                        