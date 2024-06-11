# Problem - 1614: Maximum Nesting Depth of the Parentheses
# Python3 Solution!
class Solution:
    def maxDepth(self, s: str) -> int:
        res, curDepth = 0, 0

        for i in s:
            if i == '(':
                curDepth+=1
            elif i == ')':
                curDepth-=1

            res = max(res, curDepth)

        return res

if __name__=="__main__":
    sol = Solution()

    print(sol.maxDepth("(1+(2*3)+((8)/4))+1"))
    print(sol.maxDepth("(1)+((2))+(((3)))"))