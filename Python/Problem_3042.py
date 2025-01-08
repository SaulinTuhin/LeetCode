from typing import List

# Problem - 3042. Count Prefix and Suffix Pairs I
# Python3 Solution!
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1: List[str], str2: List[str]) -> bool:
            if len(str1) > len(str2): return False
            for i in range(len(str1)):
                if str1[i] != str2[i]: return False
            for i in range(len(str1)):
                if str1[len(str1) - i - 1] != str2[len(str2) - i - 1]: return False
            return True
        
        res =  0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    res += 1
        return res
    
    
if __name__=="__main__":
    sol = Solution()
    
    print(sol.countPrefixSuffixPairs(["a","aba","ababa","aa"]))
    print(sol.countPrefixSuffixPairs(["pa","papa","ma","mama"]))
    print(sol.countPrefixSuffixPairs(["abab","ab"]))