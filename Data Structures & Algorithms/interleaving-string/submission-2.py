class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        if m + n != len(s3):
            return False
            
        memo = [[-1] * (m + 1) for _ in range(n + 1)]

        def dfs(i, j):
            cur = i + j
            if i == m and j == n:
                return True
            elif i == m:
                if s3[cur] == s2[j]:
                    memo[i][j] = dfs(i, j + 1)
                else:
                    memo[i][j] = False
            elif j == n:
                if s3[cur] == s1[i]:
                    memo[i][j] = dfs(i + 1, j)
                else:
                    memo[i][j] = False
                    
            if memo[i][j] != -1:
                return memo[i][j]

            if s3[cur] == s1[i]:
                if s3[cur] == s2[j]:
                    memo[i][j] = dfs(i + 1, j) or dfs(i, j + 1)
                else:
                    memo[i][j] = dfs(i + 1, j)
            else:
                if s3[cur] == s2[j]:
                    memo[i][j] = dfs(i, j + 1)
                else:
                    memo[i][j] = False

            return memo[i][j]

        return dfs(0, 0)