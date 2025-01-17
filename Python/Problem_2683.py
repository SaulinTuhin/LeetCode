from typing import List

# Problem - 2683. Neighboring Bitwise XOR
# Python3 Solution!
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return sum(derived) % 2 == 0

    def doesValidArrayExist_1(self, derived: List[int]) -> bool:
        res = 0
        for n in derived:
            res ^= n
        return not res


if __name__ == "__main__":
    sol = Solution()

    print(sol.doesValidArrayExist([1, 1, 0]))
    print(sol.doesValidArrayExist([1, 1]))
    print(sol.doesValidArrayExist([1, 0]))
