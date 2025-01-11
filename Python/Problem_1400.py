from typing import Counter

# Problem - 1400. Construct K Palindrome Strings
# Python3 Solution!
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        elif len(s) == k:
            return True
        
        oddCount = 0
        for freq in Counter(s).values():
            if freq % 2 != 0:
                oddCount += 1
                if oddCount > k:
                    return False
        return True


if __name__=="__main__":
    sol = Solution()
    
    print(sol.canConstruct("annabelle", 2))
    print(sol.canConstruct("leetcode", 3))
    print(sol.canConstruct("true", 4))