from typing import List

# Problem - 75: https://leetcode.com/problems/sort-colors/
# Python3 Solution!
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1
        i = 0

        def swap (i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        while i <= right:
            if nums[i] == 0:
                swap(left, i)
                left += 1
            elif nums[i] == 2:
                swap(right, i)
                right -= 1
                i -= 1
            i += 1
        

if __name__=="__main__":
    sol = Solution()

    input = [2,0,2,1,1,0]
    sol.sortColors(input)
    print(input)

    input = [2,0,1]
    sol.sortColors(input)
    print(input)