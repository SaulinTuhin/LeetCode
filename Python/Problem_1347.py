# Problem - 1347: https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/
# Python Solution!
class Solution:
    def minSteps_regular(self, s: str, t: str) -> int:
        charCount = [0] * 26
        for i in range(len(s)):
            charCount[ord(s[i]) - ord('a')] += 1
            charCount[ord(t[i]) - ord('a')] -= 1
        res = 0
        for i in range(26):
            res += charCount[i] if charCount[i] > 0 else 0
        return res

    def minSteps(self, s: str, t: str) -> int:
        res = 0
        for char in set(s):
            diff = s.count(char) - t.count(char)
            res += diff if diff > 0 else 0
        return res


if __name__=='__main__':
    sol = Solution()

    print(sol.minSteps("bab", "aba"))
    print(sol.minSteps("leetcode", "practice"))
    print(sol.minSteps("anagram", "mangaar"))