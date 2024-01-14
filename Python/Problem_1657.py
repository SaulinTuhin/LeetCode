from collections import Counter

# Problem - 1657: https://leetcode.com/problems/determine-if-two-strings-are-close/
# Python Solution!
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        freq1 = Counter(word1)
        freq2 = Counter(word2)

        return freq1.keys() == freq2.keys() and sorted(freq1.values()) == sorted(freq2.values())


if __name__=='__main__':
    sol = Solution()

    print(sol.closeStrings("abc", "bca"))
    print(sol.closeStrings("a", "aa"))
    print(sol.closeStrings("cabbba", "abbccc"))