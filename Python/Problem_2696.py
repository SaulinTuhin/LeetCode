# Problem - 2696. Minimum String Length After Removing Substrings
# Python3 Solution!
class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        stack.append(s[0])

        for i in range(1, len(s)):
            if len(stack) and (
                (s[i] == 'B' and stack[-1] == 'A') or
                (s[i] == 'D' and stack[-1] == 'C')
            ):
                stack.pop()
                continue
            stack.append(s[i])

        return len(stack)


if __name__ == "__main__":
    sol = Solution()

    print(sol.minLength("ABFCACDB"))
    print(sol.minLength("ACBBD"))
