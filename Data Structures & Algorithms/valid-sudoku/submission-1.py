class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            d = defaultdict(int)
            for col in range(9):
                val = board[row][col]
                if val != ".":
                    if d[val] != 0:
                        return False
                    else: 
                        d[val] = col + 1

        for col in range(9):
            d = defaultdict(int)
            for row in range(9):
                val = board[row][col]
                if val != ".":
                    if d[val] != 0:
                        return False
                    else: 
                        d[val] = row + 1

        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])

        return True

