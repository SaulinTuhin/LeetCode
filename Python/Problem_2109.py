from typing import List

# Problem - 2109. Adding Spaces to a String
# Python3 Solution!
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        left = 0
        for right in spaces:
            res.append(s[left:right])
            left = right
        res.append(s[left:])
        return " ".join(res)
    
    def addSpaces_slower(self, s: str, spaces: List[int]) -> str:
        res = []
        space_i = 0
        for i, c in enumerate(s):
            if space_i < len(spaces) and i == spaces[space_i]:
                res.append(' ')
                space_i += 1
            res.append(c)
        return "".join(res)


if __name__=="__main__":
    sol = Solution()
    
    print(sol.addSpaces("LeetcodeHelpsMeLearn", [8,13,15]))
    print(sol.addSpaces("icodeinpython", [1,5,7,9]))
    print(sol.addSpaces("spacing", [0,1,2,3,4,5,6]))