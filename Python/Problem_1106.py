# Problem - 1106. Parsing A Boolean Expression
# Python3 Solution!
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        for ch in expression:
            if ch == ',': continue
            
            if ch != ')': stack.append(ch)
            else:
                has_true = False
                has_false = False
                
                cur_ch = stack.pop()
                while cur_ch != '(':
                    if cur_ch == 't': has_true = True
                    elif cur_ch == 'f': has_false = True
                    cur_ch = stack.pop()
                
                operator = stack.pop()
                if operator == '&':
                    stack.append('f' if has_false else 't')
                elif operator == '|':
                    stack.append('t' if has_true else 'f')
                else:
                    stack.append('f' if has_true else 't')
        res = stack.pop()
        return True if res == 't' else False


if __name__=="__main__":
    sol = Solution()
    
    print(sol.parseBoolExpr("&(|(f))"))
    print(sol.parseBoolExpr("|(f,f,f,t)"))
    print(sol.parseBoolExpr("!(&(f,t))"))