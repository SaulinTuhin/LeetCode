from bisect import bisect_left
from typing import List

# Problem - 1671. Minimum Number of Removals to Make Mountain Array
# Python3 Solution!
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        N = len(nums)
        
        dp = []
        lis = [1] * N
        for i in range(N):
            idx = bisect_left(dp, nums[i])
            if idx == len(dp):
                dp.append(nums[i])
            else:
                dp[idx] = nums[i]
            lis[i] = len(dp)
        
        dp = []    
        lds = [1] * N
        for i in reversed(range(N)):
            idx = bisect_left(dp, nums[i])
            if idx == len(dp):
                dp.append(nums[i])
            else:
                dp[idx] = nums[i]
            lds[i] = len(dp)
                    
        res = N
        for i in range(1, N - 1):
            if lis[i] > 1 and lds[i] > 1:
                res = min(res, N - lis[i] - lds[i] + 1)
        return res
    
    def minimumMountainRemovals_LIS(self, nums: List[int]) -> int:
        N = len(nums)
        
        lis = [1] * N
        for i in range(N):
            for j in range(i):
                if nums[j] < nums[i]:
                    lis[i] = max(lis[i], 1 + lis[j])
        lds = [1] * N
        for i in reversed(range(N)):
            for j in range(i + 1, N):
                if nums[j] < nums[i]:
                    lds[i] = max(lds[i], 1 + lds[j])
                    
        res = N
        for i in range(1, N - 1):
            if lis[i] > 1 and lds[i] > 1:
                res = min(res, N - lis[i] - lds[i] + 1)
        return res
    
    
if __name__=="__main__":
    sol = Solution()
    
    print(sol.minimumMountainRemovals([1,3,1]))
    print(sol.minimumMountainRemovals([2,1,1,5,6,2,3,1]))