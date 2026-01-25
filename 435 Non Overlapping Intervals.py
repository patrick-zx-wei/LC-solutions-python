class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        def value(a: List[int]) -> int:
            return a[1] * 50001 - a[0]
        intervals.sort(key=value)
        allowed = 0
        lastHigh = -50001
        print(intervals)
        for interval in intervals:
            if lastHigh <= interval[0]:
                allowed += 1
                lastHigh = interval[1]
        return len(intervals) - allowed
