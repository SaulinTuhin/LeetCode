from typing import List

# Problem - 2501. Longest Square Streak in an Array
# Python3 Solution!
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        mp = {}
        res = -1
        for n in nums:
            if n * n in mp:
                mp[n] = mp[n * n] + 1
                res = max(res, mp[n])
            else:
                mp[n] = 1
        return res    


if __name__=="__main__":
    sol = Solution()
    
    print(sol.longestSquareStreak([4,3,6,16,8,2]))
    print(sol.longestSquareStreak([2,3,5,6,7]))