# Problem - 2938. Separate Black and White Balls
# Python3 Solution!
class Solution:
    def minimumSteps(self, s: str) -> int:
        res = left = 0
        for right in range(len(s)):
            if s[right] == '0':
                res += (right - left)
                left += 1
        return res
    
    
if __name__=="__main__":
    sol = Solution()
    
    print(sol.minimumSteps("101"))
    print(sol.minimumSteps("100"))
    print(sol.minimumSteps("0111"))