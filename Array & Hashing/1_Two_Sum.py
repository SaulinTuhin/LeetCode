from typing import List

class Solution:
    def twoSum_0(self, nums: List[int], target: int) -> List[int]:
        """
        Good starting point for interview, brute force.
        O(n^2) -> Time
        O(1) -> Space
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return [-1, -1]
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        O(n) -> Time & Space
        """
        seen = {}

        for i, n in enumerate(nums):
            required = target - n
            if required in seen:
                return [i, seen[required]]
            seen[n] = i
        
        return [-1, -1]
    

if __name__=="__main__":
    sol = Solution()

    print(sol.twoSum([2,7,11,15], 9))
    print(sol.twoSum([3,2,4], 6))
    print(sol.twoSum([3,3], 6))