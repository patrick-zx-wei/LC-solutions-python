class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = [[False for _ in range(len(heights[0]))] for _ in range(len(heights))]
        atlantic = [[False for _ in range(len(heights[0]))] for _ in range(len(heights))]
        
        def traverse(row: int, col: int, isPacific: bool):
            if isPacific:
                pacific[row][col] = True
                if row > 0 and not pacific[row - 1][col] and heights[row][col] <= heights[row - 1][col]:
                    traverse(row - 1, col, True)
                if row < len(heights) - 1 and not pacific[row + 1][col] and heights[row][col] <= heights[row + 1][col]:
                    traverse(row + 1, col, True)
                if col > 0 and not pacific[row][col - 1] and heights[row][col] <= heights[row][col - 1]:
                    traverse(row, col - 1, True)
                if col < len(heights[0]) - 1 and not pacific[row][col + 1] and heights[row][col] <= heights[row][col + 1]:
                    traverse(row, col + 1, True)
                
            else:
                atlantic[row][col] = True
                if row > 0 and not atlantic[row - 1][col] and heights[row][col] <= heights[row - 1][col]:
                    traverse(row - 1, col, False)
                if row < len(heights) - 1 and not atlantic[row + 1][col] and heights[row][col] <= heights[row + 1][col]:
                    traverse(row + 1, col, False)
                if col > 0 and not atlantic[row][col - 1] and heights[row][col] <= heights[row][col - 1]:
                    traverse(row, col - 1, False)
                if col < len(heights[0]) - 1 and not atlantic[row][col + 1] and heights[row][col] <= heights[row][col + 1]:
                    traverse(row, col + 1, False)
                    
        for i in range(len(heights)):
            traverse(i, 0, True)
            traverse(i, len(heights[0]) - 1, False)
        for j in range(len(heights[0])):
            traverse(0, j, True)
            traverse(len(heights) - 1, j, False)

        points = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if pacific[i][j] and atlantic[i][j]:
                    temp = [i, j]
                    points.append(temp)
        
        return points
        
                    
