class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        highest = -2000000000
        ongoing = 0
        for num in nums:
            if num >= 0 and ongoing <= 0:
                ongoing = num
            elif num > 0 and ongoing > 0:
                ongoing += num
            elif num < 0 and ongoing <= 0:
                ongoing = num
            else:
                ongoing += num
            highest = max(ongoing, highest)
            print(ongoing)

        return highest
