from typing import List

# Problem - 2425. Bitwise XOR of All Pairings
# Python3 Solution!
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)

        res = 0
        if m % 2 == 1:
            for num in nums1:
                res ^= num
        
        if n % 2 == 1:
            for num in nums2:
                res ^= num

        return res


if __name__=="__main__":
    sol = Solution()
    
    print(sol.xorAllNums([2,1,3], [10,2,5,0]))
    print(sol.xorAllNums([1,2], [3,4]))