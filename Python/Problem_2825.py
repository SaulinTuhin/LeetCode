# Problem - 2825. Make String a Subsequence Using Cyclic Increments
# Python3 Solution!
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        # if len(str2) > len(str1): return False
        i, j = 0, 0
        while i < len(str1):
            if j < len(str2) and (ord(str2[j]) - ord(str1[i])) % 26 < 2:
                j += 1
            i += 1
        return j == len(str2)


if __name__=="__main__":
    sol = Solution()
    
    print(sol.canMakeSubsequence("abc", "ad"))
    print(sol.canMakeSubsequence("zc", "ad"))
    print(sol.canMakeSubsequence("ab", "d"))