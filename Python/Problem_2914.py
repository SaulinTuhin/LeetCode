# Problem - 2914. Minimum Number of Changes to Make Binary String Beautiful
# Python3 Solution!
class Solution:
    def minChanges(self, s: str) -> int:
        res = 0        
        for i in range(0, len(s), 2):
            if s[i] != s[i + 1]:
                res += 1
        return res


if __name__=="__main__":
    sol = Solution()
    
    print(sol.minChanges("1001"))
    print(sol.minChanges("10"))
    print(sol.minChanges("0000"))