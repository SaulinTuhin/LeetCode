from typing import List

# Problem - 2554. Maximum Number of Integers to Choose From a Range I
# Python3 Solution!
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        cur_sum, res = 0, 0
        for i in range(1, n + 1):
            if i not in banned:
                cur_sum += i
                if cur_sum > maxSum:
                    break
                res += 1
        return res


if __name__ == "__main__":
    sol = Solution()

    print(sol.maxCount([1, 6, 5], 5, 6))
    print(sol.maxCount([1, 2, 3, 4, 5, 6, 7], 8, 1))
    print(sol.maxCount([11], 7, 50))
