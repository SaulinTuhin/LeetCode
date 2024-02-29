from typing import Counter, List

# Problem - 1239: https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
# Python3 Solution!
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        charSet = set()

        def isDuplicate(charSet, s):
            c = Counter(charSet) + Counter(s)
            return max(c.values()) > 1

        def backtrack(i):
            if i == len(arr):
                return len(charSet)
            res = 0
            if not isDuplicate(charSet, arr[i]):
                for c in arr[i]:
                    charSet.add(c)
                res = backtrack(i + 1)
                for c in arr[i]:
                    charSet.remove(c)
            return max(res, backtrack(i + 1))
        
        return backtrack(0)


if __name__=='__main__':
    sol = Solution()

    print(sol.maxLength(["un","iq","ue"]))
    print(sol.maxLength(["cha","r","act","ers"]))
    print(sol.maxLength(["abcdefghijklmnopqrstuvwxyz"]))