from typing import List
import heapq
from math import ceil

# Problem - 2530. Maximal Score After Applying K Operations
# Python3 Solution!
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        max_heap = [-n for n in nums]
        heapq.heapify(max_heap)
        
        res = 0
        while k:
            n = -heapq.heappop(max_heap)
            res += n
            heapq.heappush(max_heap, -ceil(n / 3))
            k -= 1
        return res
    
    
if __name__=="__main__":
    sol = Solution()
    
    print(sol.maxKelements([10,10,10,10,10], 5))
    print(sol.maxKelements([1,10,3,3,3], 3))