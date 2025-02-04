from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        cur_sum = res = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cur_sum += nums[i]
            else:
                cur_sum = nums[i]
            res = max(res, cur_sum)
        return res


if __name__=="__main__":
    sol = Solution()
    
    print(sol.maxAscendingSum([10,20,30,5,10,50]))
    print(sol.maxAscendingSum([10,20,30,40,50]))
    print(sol.maxAscendingSum([12,17,15,13,10,11,12]))