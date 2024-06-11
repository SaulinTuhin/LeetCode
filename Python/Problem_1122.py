from collections import defaultdict
from typing import List

# Problem - 1122: https://leetcode.com/problems/relative-sort-array/
# Python3 Solution!
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
       arr1_freq = defaultdict(int)
       arr2_set = set(arr2)

       last = []
       for num in arr1:
           if num not in arr2_set:
               last.append(num)
           arr1_freq[num] += 1
       last.sort()
       
       res = []
       for num in arr2:
           for _ in range(arr1_freq[num]):
               res.append(num)

       return res + last

if __name__=="__main__":
    sol = Solution()

    print(sol.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))
    print(sol.relativeSortArray([28,6,22,8,44,17], [22,28,8,6]))