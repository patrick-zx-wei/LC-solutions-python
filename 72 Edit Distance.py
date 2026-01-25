class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        x = len(word1) 
        y = len(word2)
        distance = [[-1 for _ in range(y+ 1)] for _ in range(x + 1)]
        #fill in basecases
        for i in range(y + 1):
            distance[x][y - i] = i
        for i in range(x + 1):
            distance[x - i][y] = i

        #fill bottom up
        for i in range(x - 1, -1, -1):
            for j in range(y - 1, -1, -1):
                if word1[i] == word2[j]:
                    distance[i][j] = distance[i+1][j+1]
                else:
                    distance[i][j] = 1 + min(distance[i + 1][j], distance[i + 1][j + 1], distance[i][j + 1])
        return distance[0][0]            
            
        
