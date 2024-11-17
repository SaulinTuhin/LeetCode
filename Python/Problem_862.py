from collections import deque
from typing import List

# Problem - 862. Shortest Subarray with Sum at Least K
# Python3 Solution!
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        res = float("inf")
        q = deque()
        cur_prefix_sum = 0
        
        for right in range(len(nums)):
            cur_prefix_sum += nums[right]
            if cur_prefix_sum >= k:
                res = min(res, right + 1)
            
            while q and cur_prefix_sum - q[0][0] >= k:
                prev_prefix_sum, left = q.popleft()
                res = min(res, right - left)
            
            while q and q[-1][0] >= cur_prefix_sum:
                q.pop()
            q.append((cur_prefix_sum, right))
            
        return -1 if res == float("inf") else res


if __name__=="__main__":
    sol = Solution()
    
    print(sol.shortestSubarray([1], 1))
    print(sol.shortestSubarray([1,2], 4))
    print(sol.shortestSubarray([2,-1,2], 3))