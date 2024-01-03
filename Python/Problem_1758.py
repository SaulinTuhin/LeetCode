# Problem - 1758: https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/
# Lang: Python3
class Solution:
    def minOperations(self, s: str) -> int:
        operations = 0

        for i in range(len(s)):
            if i % 2 == 0:
                operations += 1 if s[i] != '0' else 0
            else:
                operations += 1 if s[i] != '1' else 0

        return min(operations, len(s) - operations)


if __name__=="__main__":
    sol = Solution()

    print(sol.minOperations("0100"))
    print(sol.minOperations("10"))
    print(sol.minOperations("1111"))