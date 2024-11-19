from typing import List
from collections import defaultdict

# Problem - 2461. Maximum Sum of Distinct Subarrays With Length K
# Python3 Solution!
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        nums_count = defaultdict(int)
        duplicate_count = 0
        cur_sum = 0
        for i in range(k):
            nums_count[nums[i]] += 1
            cur_sum += nums[i]
            if nums_count[nums[i]] > 1:
                duplicate_count += 1
        
        for i in range(k, n):
            if duplicate_count == 0:
                res = max(res, cur_sum)
            
            if nums_count[nums[i - k]] > 1:
                duplicate_count -= 1
            nums_count[nums[i - k]] -= 1
            cur_sum -= nums[i - k]
            
            nums_count[nums[i]] += 1
            cur_sum += nums[i]
            if nums_count[nums[i]] > 1:
                duplicate_count += 1
                
        return max(res, cur_sum) if duplicate_count == 0 else res


if __name__=="__main__":
    sol = Solution()
    
    print(sol.maximumSubarraySum([1,5,4,2,9,9,9], 3))
    print(sol.maximumSubarraySum([4,4,4], 3))
    print(sol.maximumSubarraySum([1,1,1,7,8,9], 3))