from typing import List

# Notes:
# 1. Array being sorted is a red herring, so ignore
# 2. The answers are the `k`s that will maximize the XOR
#    of `len(nums) - i` with k. Res is not the XOR, but `k`

# Problem - 1829. Maximum XOR for Each Query
# Python3 Solution!
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xor_nums = 0
        for n in nums:
            xor_nums = xor_nums ^ n
        
        res = []
        mask = (1 << maximumBit) - 1
        for n in reversed(nums):
            res.append(xor_nums ^ mask)
            xor_nums = xor_nums ^ n
        return res


if __name__=="__main__":
    sol = Solution()
    
    print(sol.getMaximumXor([0,1,1,3], 2))
    print(sol.getMaximumXor([2,3,4,7], 3))
    print(sol.getMaximumXor([0,1,2,2,5,7], 3))