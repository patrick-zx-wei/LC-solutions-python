class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = (int)(total / 2)
        achieveable = [False] * (target + 1)

        achieveable[0] = True
        for num in nums:
            for i in range(target, num - 1, -1):
                if achieveable[i - num]:
                    achieveable[i] = True

        return achieveable[target]
