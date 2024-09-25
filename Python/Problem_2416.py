from typing import List, DefaultDict

# Problem - 2416. Sum of Prefix Scores of Strings
# Python3 Solution!
# Trie/Prefix Tree solution
class TrieNode:
    def __init__(self) -> None:
        self.children = [None] * 26
        self.count = 0

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
        
    def insert(self, w) -> None:
        cur = self.root
        for c in w:
            i = ord(c) - ord('a')
            if not cur.children[i]:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
            cur.count += 1

    def getScore(self, w) -> int:
        cur = self.root
        score = 0
        for c in w:
            i = ord(c) - ord('a')
            cur = cur.children[i]
            score += cur.count
        return score

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        res = []
        trie = Trie()

        for w in words:
            trie.insert(w)

        for w in words:
            res.append(trie.getScore(w))

        return res


# Hashmap solution
class Solution1:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        res = []
        prefix_freq = DefaultDict(int)

        for w in words:
            for i in range(len(w)):
                prefix_freq[w[:i+1]] += 1

        for w in words:
            score = 0
            for i in range(len(w)):
                score += prefix_freq[w[:i+1]]
            res.append(score)
        return res


if __name__=='__main__':
    sol = Solution()

    print(sol.sumPrefixScores(["abc","ab","bc","b"]))
    print(sol.sumPrefixScores(["abcd"]))