class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
    #to check if a soln is valid, it will be sufficient to check the middle squares
    #and then check col between top and bottom to avoid edge cases
        board = [["." for _ in range(n)] for _ in range(n)]
        solns = []

        cols = set()
        neg_diagonal = set()
        pos_diagonal = set()

        def check(row: int, col: int) -> bool:
            return not (col in cols or row + col in pos_diagonal or row - col in neg_diagonal)

        #recursively form n! boards
        def brute(row: int):
            if row == n:
                soln = []
                for line in board:
                    soln.append("".join(line))
                solns.append(soln)
                return
            for col in range(n):
                if check(row, col):
                    board[row][col] = "Q"
                    cols.add(col)
                    neg_diagonal.add(row - col)
                    pos_diagonal.add(row + col)
                    brute(row + 1)
                    pos_diagonal.remove(row + col)
                    neg_diagonal.remove(row - col)
                    cols.remove(col)
                    board[row][col] = "."
            return

        brute(0)
        return solns
                
