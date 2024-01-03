from typing import DefaultDict, List

# Problem - 1897: https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/
# Python3 Problem!
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        # ch_frequency = [0] * 26
        ch_frequency = DefaultDict(int)

        for word in words:
            for ch in word:
                ch_frequency[ch] += 1

        for ch in ch_frequency:
            if ch_frequency[ch] % len(words):
                return False
            
        return True


if __name__=="__main__":
    sol = Solution()

    print(sol.makeEqual(["abc","aabc","bc"]))
    print(sol.makeEqual(["ab","a"]))