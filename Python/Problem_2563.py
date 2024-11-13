from typing import List
from bisect import bisect_left

# Problem - 2563. Count the Number of Fair Pairs
# Python3 Solution!
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums)):
            if upper - nums[i] < nums[i]:
                break
            res += (
                bisect_left(nums, upper - nums[i] + 1, i + 1) -
                bisect_left(nums, lower - nums[i], i + 1)
            )
        return res


if __name__=="__main__":
    sol = Solution()
    
    print(sol.countFairPairs([0,1,7,4,4,5], 3, 6))
    print(sol.countFairPairs([1,7,9,2,5], 11, 11))
    print(sol.countFairPairs([0,0,0,0,0,0], 0, 0))