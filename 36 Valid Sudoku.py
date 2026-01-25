class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[False for _ in range(9)] for _ in range(9)]
        cols = [[False for _ in range(9)] for _ in range(9)]
        boxes = [[[False for _ in range(9)] for _ in range(3)] for _ in range(3)]

        for i, row in enumerate(board):
            for j, square in enumerate(row):
                if square != ".":
                    value = int(square) - 1
                    if rows[i][value] or cols[j][value] or boxes[math.floor(i/3)][math.floor(j/3)][value]:
                        return False
                    rows[i][value] = True
                    cols[j][value] = True
                    boxes[math.floor(i/3)][math.floor(j/3)][value] = True
        return True
