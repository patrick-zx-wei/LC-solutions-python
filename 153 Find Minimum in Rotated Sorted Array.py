class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        mid = left + math.floor((right - left) / 2)
        if nums[left] < nums[mid] and nums[mid] < nums[right]:
            return nums[left]
        while left < right - 1:
            if nums[mid] > nums[left]: #swap is in the right side 
                left = mid
            else:
                right = mid
            mid = left + math.floor((right - left) / 2)
        
        if nums[left] < nums[right]:
             return nums[left] 
        else:
            return nums[right]
