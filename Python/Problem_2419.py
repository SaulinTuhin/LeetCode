from typing import List

# Problem - 2419: Longest Subarray With Maximum Bitwise AND
# Python3 Solution!
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_size, cur_size, cur_max = 0, 0, 0
        for i in nums:
            if i > cur_max:
                cur_max = i
                max_size = 0
                cur_size = 1
            elif i == cur_max:
                cur_size += 1
            else:
                cur_size = 0
            max_size = max(max_size, cur_size)

        return max_size


if __name__=="__main__":
    sol = Solution()

    print(sol.longestSubarray([1,2,3,3,2,2]))
    print(sol.longestSubarray([1,2,3,4]))