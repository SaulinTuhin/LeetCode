# Problem - 921. Minimum Add to Make Parentheses Valid
# Python3 Solution!
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        extra_open, extra_close = 0, 0
        
        for p in s:
            if p == '(':
                extra_open += 1
            else:
                if extra_open == 0:
                    extra_close += 1
                else:
                    extra_open -= 1
        
        return extra_open + extra_close
    
    
if __name__=="__main__":
    sol = Solution()
    
    print(sol.minAddToMakeValid("())"))
    print(sol.minAddToMakeValid("((("))