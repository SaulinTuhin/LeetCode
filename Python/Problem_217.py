from typing import List
from collections import defaultdict

# Problem - 217. Contains Duplicate
# Python3 Solution!
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq_map = defaultdict(int)
        for n in nums:
            freq_map[n] += 1
            if freq_map[n] > 1: return True
        return False



if __name__=="__main__":
    sol = Solution()
    
    print(sol.containsDuplicate([1,2,3,1]))
    print(sol.containsDuplicate([1,2,3,4]))
    print(sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))