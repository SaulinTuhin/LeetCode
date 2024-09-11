# Problem - 2220: Minimum Bit Flips to Convert Number
# Python3 Solution!
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res = 0

        x = start ^ goal
        while x:
            x = x & (x - 1)
            res += 1

        return res
    
    def minBitFlips_1(self, start: int, goal: int) -> int:
        res = 0

        x = start ^ goal
        while x:
            res += (x & 1)
            x = x >> 1

        return res


if __name__=="__main__":
    sol = Solution()

    print(sol.minBitFlips(10, 7))
    print(sol.minBitFlips(3, 4))