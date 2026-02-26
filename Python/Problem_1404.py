# Problem - 1404. Number of Steps to Reduce a Number in Binary Representation to One
# Python3 Solution!
class Solution:
    def numSteps(self, s: str) -> int:
        carry = 0
        res = 0
        for i in range(len(s) - 1, 0, -1):
            if not carry:
                if s[i] == "1":
                    res += 2
                    carry = 1
                else:
                    res += 1
            else:
                if s[i] == "1":
                    res += 1
                else:
                    res += 2
        return res + carry


if __name__=="__main__":
    sol = Solution()

    print(sol.numSteps("1101"))
    print(sol.numSteps("10"))
    print(sol.numSteps("1"))