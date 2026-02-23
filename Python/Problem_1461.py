# Problem - 1461. Check If a String Contains All Binary Codes of Size K
# Python3 Solution!
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        substrSet = set()
        for i in range(len(s) - k + 1):
            substrSet.add(s[i : i + k])
            if len(substrSet) == 2 ** k:
                return True
        return False


if __name__=="__main__":
    sol = Solution()

    print(sol.hasAllCodes("00110110", 2))
    print(sol.hasAllCodes("0110", 1))
    print(sol.hasAllCodes("0110", 2))