class Solution:
    def maxScore(self, s: str) -> int:
        zeroes, ones = 0, 0

        for i in range(len(s)):
            if int(s[i]) == 1:
                ones += 1

        max_score = 0
        for i in range (1, len(s)):
            if int(s[i]) == 1:
                ones -= 1
            else:
                zeroes += 1

            if ones + zeroes > max_score:
                max_score = ones + zeroes
        
        return max_score

if __name__=="__main__":
    sol = Solution()

    print(sol.maxScore("011101"))
    print(sol.maxScore("00111"))
    print(sol.maxScore("1111"))