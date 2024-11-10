from typing import List

# Problem - 3097. Shortest Subarray With OR at Least K II
# Python3 Solution!
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        min_length = len(nums) + 1
        cur_bits = [0] * 32
        
        def bit_opeation(n: int, delta: int):
            for i in range(32):
                if n & (1 << i):
                    cur_bits[i] += delta
        
        def get_num():
            num = 0
            for i in range(32):
                if cur_bits[i]:
                    num |= 1 << i
            return num
        
        left = right = 0
        while right < len(nums):
            bit_opeation(nums[right], 1)
            while left <= right and get_num() >= k:
                bit_opeation(nums[left], -1)
                min_length = min(min_length, right - left + 1)
                left += 1
            right += 1
        return -1 if min_length > len(nums) else min_length


if __name__=="__main__":
    sol = Solution()
    
    print(sol.minimumSubarrayLength([1,2,3], 2))
    print(sol.minimumSubarrayLength([2,1,8], 10))
    print(sol.minimumSubarrayLength([1,2], 0))