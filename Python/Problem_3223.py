from collections import Counter

# Problem - 3223. Minimum Length of String After Operations
# Python3 Solution!
class Solution:
    def minimumLength(self, s: str) -> int:
        freq = Counter(s)
        res = 0
        for f in freq.values():
            if f % 2 == 1:
                res += 1
            else:
                res += 2
        return res


if __name__=="__main__":
    sol = Solution()
    
    print(sol.minimumLength("abaacbcbb"))
    print(sol.minimumLength("aa"))