from typing import List

# Problem - 3043: Find the Length of the Longest Common Prefix
# Python3 Solution!
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefix = set()
        for i in arr1:
            while i:
                prefix.add(i)
                i = i//10
        
        res = 0
        for i in arr2:
            while i and i not in prefix:
                i = i // 10            
            if i:
                res = max(res, len(str(i)))

        return res


if __name__=='__main__':
    sol = Solution()

    print(sol.longestCommonPrefix([1,10,100], [1000]))
    print(sol.longestCommonPrefix([1,2,3], [4,4,4]))