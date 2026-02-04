class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort(reverse=True) #this way we know walking forward is always possible
        combinations = []
        def traverse(index: int, total: int, curr: List[int]):
            if total > target:
                return
            if total == target:
                combinations.append(curr[:])
                return
            for i in range(index, len(nums)):
                curr.append(nums[i])
                returned = traverse(i, total + nums[i], curr)
                curr.pop()

        traverse(0, 0, [])
        return combinations
