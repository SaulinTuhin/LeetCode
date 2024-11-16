from typing import List

# Problem - 3254. Find the Power of K-Size Subarrays I
# Python3 Solution!
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1: return nums
        
        res = []
        consecutive_count = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                consecutive_count += 1
            else:
                consecutive_count = 1
            
            if i >= k - 1:
                res.append(nums[i] if consecutive_count >= k else -1)
        return res


if __name__=="__main__":
    sol = Solution()
    
    print(sol.resultsArray([1,2,3,4,3,2,5], 3))
    print(sol.resultsArray([2,2,2,2,2], 4))
    print(sol.resultsArray([3,2,3,2,3,2], 2))