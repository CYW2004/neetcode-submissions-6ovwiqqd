class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        len2 = len(s2) 

        if len1 > len2:
            return False

        for l in range(0, len2 - len1 + 1):
            r = l + len1
            if sorted(s1) == sorted(s2[l:r]):
                return True

        return False

