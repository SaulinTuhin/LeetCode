# Problem - 2116. Check if a Parentheses String Can Be Valid
# Python3 Solution!
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        unlocked = []
        stack = []
        for i in range(len(s)):
            if locked[i] == "0":
                unlocked.append(i)
            elif s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if stack:
                    stack.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False
            
        while stack and unlocked and stack[-1] < unlocked[-1]:
            stack.pop()
            unlocked.pop()
        
        return not stack


if __name__=="__main__":
    sol = Solution()
    
    print(sol.canBeValid("))()))", "010100"))
    print(sol.canBeValid("()()", "0000"))
    print(sol.canBeValid(")", "0"))