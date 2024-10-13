from typing import List
import heapq

# Problem - 632. Smallest Range Covering Elements from K Lists
# Python3 Solution!
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        left = right = nums[0][0]
        min_heap = []
        for i in range(k):
            cur_n = nums[i][0]
            right = max(right, cur_n)
            heapq.heappush(min_heap, (cur_n, i, 0)) # (cur_n, row, col)
        left = min_heap[0][0]
        
        res = [left, right]
        while True:
            cur_n, row, col = heapq.heappop(min_heap)
            col += 1
            if col == len(nums[row]):
                return res
            
            next_n = nums[row][col]
            heapq.heappush(min_heap, (next_n, row, col))
            right = max(right, next_n)
            left = min_heap[0][0]
            if right - left < res[1] - res[0]:
                res = [left, right]
            
        
        
if __name__=="__main__":
    sol = Solution()
    
    print(sol.smallestRange([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]))
    print(sol.smallestRange([[1,2,3],[1,2,3],[1,2,3]]))