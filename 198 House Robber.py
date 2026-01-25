class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [[0 for _ in range(2)] for _ in range(len(nums))]
        #top is rob todfay, bottom is not rob today
        dp[0][0] = nums[0]
        for i in range(1, len(nums)):
            dp[i][0] = dp[i-1][1] + nums[i]
            dp[i][1] = dp[i-1][0]
            if dp[i][1] > dp[i][0]:
                dp[i][0] = dp[i][1]
        return max(dp[len(nums)-1][0], dp[len(nums)-1][1])
