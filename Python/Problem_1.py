from typing import List
from collections import defaultdict

# Problem - 1. Two Sum
# Python3 Solution!
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq_map = defaultdict(int)
        for i, n in enumerate(nums):
            if (target - n) in freq_map:
                return [freq_map[target-n], i]
            freq_map[n] = i


if __name__=="__main__":
    sol = Solution()
    
    print(sol.twoSum([2,7,11,15], 9))
    print(sol.twoSum([3,2,4], 6))
    print(sol.twoSum([3,3], 6))