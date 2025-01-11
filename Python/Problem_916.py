from typing import List

# Problem - 916. Word Subsets
# Python3 Solution!
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def count(word: str) -> list[int]:
            freq = [0] * 26
            for c in word:
                freq[ord(c) - ord('a')] += 1
            return freq
        
        maxW2Freq = [0] * 26
        for word in words2:
            for i, c in enumerate(count(word)):
                maxW2Freq[i] = max(maxW2Freq[i], c)
        
        res = []
        for word in words1:
            if all(x>=y for x, y in zip(count(word), maxW2Freq)):
                res.append(word)
        return res


if __name__=="__main__":
    sol = Solution()
    
    print(sol.wordSubsets(["amazon","apple","facebook","google","leetcode"], ["e", "o"]))
    print(sol.wordSubsets(["amazon","apple","facebook","google","leetcode"], ["lc", "eo"]))
    print(sol.wordSubsets(["acaac","cccbb","aacbb","caacc","bcbbb"], ["c","cc","b"]))