# Problem - 1544: Make The String Great
# Python3 Solution!
class Solution:
    def makeGood(self, s: str) -> str:
        res = []
        for i in s:
            if res and abs(ord(res[-1]) - ord(i)) == 32:
                res.pop()
            else:
                res.append(i)

        return "".join(res)

if __name__=="__main__":
    sol = Solution()

    print(sol.makeGood("leEeetcode"))
    print(sol.makeGood("abBAcC"))
    print(sol.makeGood("s"))