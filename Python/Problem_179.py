from functools import cmp_to_key
from typing import List

# Problem - 179: Largest Number
# Python3 Solution!
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, n in enumerate(nums):
            nums[i] = str(nums[i])

        def cmp(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1

        nums = sorted(nums, key=cmp_to_key(cmp))

        return str(int("".join(nums)))


if __name__=="__main__":
    sol = Solution()
    
    print(sol.largestNumber([10,2]))
    print(sol.largestNumber([3,30,34,5,9]))