from typing import List

# Problem - 2406. Divide Intervals Into Minimum Number of Groups
# Python3 Solution!
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start_intervals, end_intervals = [], []
        for s, e in intervals:
            start_intervals.append(s)
            end_intervals.append(e)
        start_intervals.sort()
        end_intervals.sort()
        
        start_i, end_i = 0, 0
        res = 0
        while start_i < len(intervals):
            if start_intervals[start_i] <= end_intervals[end_i]:
                start_i += 1
            else:
                end_i += 1
            res = max(res, start_i - end_i)
        return res
    
    
if __name__=="__main__":
    sol = Solution()
    
    print(sol.minGroups([[5,10],[6,8],[1,5],[2,3],[1,10]]))
    print(sol.minGroups([[1,3],[5,6],[8,10],[11,13]]))