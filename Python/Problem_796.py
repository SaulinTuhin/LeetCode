# Problem - 796. Rotate String
# Python3 Solution!
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if (s+s).find(goal) != -1:
            return True
        return False


if __name__=="__main__":
    sol = Solution()
    
    print(sol.rotateString("abcde", "cdeab"))
    print(sol.rotateString("abcde", "abced"))