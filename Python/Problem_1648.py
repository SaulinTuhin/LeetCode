from typing import List

# Problem - 1648: Count the Number of Consistent Strings
# Python3 Solution!
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)

        res = len(words)
        for word in words:
            for char in word:
                if char not in allowed:
                    res -= 1
                    break

        return res


if __name__=="__main__":
    sol = Solution()

    print(sol.countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"]))
    print(sol.countConsistentStrings("abc", ["a","b","c","ab","ac","bc","abc"]))
    print(sol.countConsistentStrings("cad", ["cc","acd","b","ba","bac","bad","ac","d"]))