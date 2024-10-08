# Problem - 1963. Minimum Number of Swaps to Make the String Balanced
# Python3 Solution!
class Solution:
    def minSwaps(self, s: str) -> int:
        extra_close = 0
        max_extra_close = 0

        for c in s:
            if c == '[':
                extra_close -= 1
            else:
                extra_close += 1
            max_extra_close = max(max_extra_close, extra_close)

        return (max_extra_close + 1) // 2


if __name__ == "__main__":
    sol = Solution()

    print(sol.minSwaps("][]["))
    print(sol.minSwaps("]]][[["))
    print(sol.minSwaps("[]"))
