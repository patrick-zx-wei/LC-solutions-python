class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = [0 for _ in range(len(cost) + 1)]
        for step in range(2, len(cost) + 1, 1):
            min_cost[step] = min(min_cost[step - 2] + cost[step - 2], min_cost[step - 1] + cost[step - 1])
        return min_cost[len(cost)]
      
