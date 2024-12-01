from typing import List
from collections import Counter

class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        nums_counter = Counter(nums)
        res = float('-inf')
        total = sum(nums)
        for i in range(len(nums)):
            remaining = total - nums[i]
            if remaining % 2 == 0:
                nums_counter[nums[i]] -= 1
                if nums_counter[remaining // 2] > 0:
                    res = max(res, nums[i])
                nums_counter[nums[i]] += 1
        return res

if __name__=="__main__":
    sol = Solution()
    
    print(sol.getLargestOutlier([2,3,5,10]))
    print(sol.getLargestOutlier([-2,-1,-3,-6,4]))
    print(sol.getLargestOutlier([1,1,1,1,1,5,5]))
    print(sol.getLargestOutlier([-108,-108,-517]))
    print(sol.getLargestOutlier([6,-31,50,-35,41,37,-42,13]))