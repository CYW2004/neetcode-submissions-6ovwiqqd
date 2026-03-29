class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        isChecked = [False] * len(s)

        def isWord(word, pointer):
            n = len(word)
            for i in range(0, n, 1):
                if isChecked[pointer + i]:
                    continue
                if word[0:i + 1] in wordDict:
                    isChecked[pointer + i] = True
                    if i == n - 1:
                        return True
                    elif isWord(word[i + 1:n], pointer + i + 1):
                        return True
            return False

        return isWord(s, 0)