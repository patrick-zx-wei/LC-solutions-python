class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found = [False] * 3
        for trip in triplets:
            if not found[0] and trip[0] == target[0] and trip[1] <= target[1] and trip[2] <= target[2]:
                found[0] = True
            if not found[1] and trip[1] == target[1] and trip[0] <= target[0] and trip[2] <= target[2]:
                found[1] = True
            if not found[2] and trip[2] == target[2] and trip[0] <= target[0] and trip[1] <= target[1]:
                found[2] = True
        return found[0] and found[1] and found[2]
