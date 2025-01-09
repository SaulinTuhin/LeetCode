from typing import List

# Problem - 2185. Counting Words With a Given Prefix
# Python3 Solution!
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0
        for word in words:
            if len(word) >= len(pref) and word.startswith(pref):
                res += 1
        return res
    
    def prefixCount_1(self, words: List[str], pref: str) -> int:
        res = 0
        for word in words:
            if len(word) < len(pref): continue

            for i in range(len(pref)):
                if word[i] != pref[i]:
                    res -= 1
                    break
            res += 1
        return res


if __name__=="__main__":
    sol = Solution()
    
    print(sol.prefixCount(["pay","attention","practice","attend"], "at"))
    print(sol.prefixCount(["leetcode","win","loops","success"], "code"))