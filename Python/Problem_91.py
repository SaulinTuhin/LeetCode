# Problem - 91: https://leetcode.com/problems/decode-ways/
# Python3
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)

        dp[n] = 1
        for i in range(n - 1, -1, -1):
            if (s[i] != '0'): dp[i] += dp[i + 1]

            if (i+1 < n and (s[i] == '1' or (s[i] == '2' and s[i + 1] <= '6'))): dp[i] += dp[i + 2]
        
        return dp[0]


if __name__=="__main__":
    sol = Solution()

    print(sol.numDecodings("12"))
    print(sol.numDecodings("226"))
    print(sol.numDecodings("06"))