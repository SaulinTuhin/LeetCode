from typing import List

# Problem - 198: https://leetcode.com/problems/house-robber/
# Python3 Solution!
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2_max, prev_max = 0, 0

        for cur in nums:
            temp = max(cur + prev2_max, prev_max)
            prev2_max = prev_max
            prev_max = temp
        return prev_max


if __name__=='__main__':
    sol = Solution()

    print(sol.rob([1,2,3,1]))
    print(sol.rob([2,7,9,3,1]))