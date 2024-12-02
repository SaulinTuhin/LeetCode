# Problem - 1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence
# Python3 Solution!
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        i, j, word = 0, 0, 1
        while i < len(sentence):
            if sentence[i] == searchWord[j]:
                i += 1
                j += 1
                if j == len(searchWord):
                    return word
            elif sentence[i] == ' ':
                i += 1
                j = 0
                word += 1
            else:
                while i < len(sentence) and sentence[i] != ' ':
                    i += 1
        return -1
    
    def isPrefixOfWord_pythonic(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split()
        n = len(searchWord)
        for i, word in enumerate(sentence):
            if searchWord == word[:n]:
                return i + 1
        return -1


if __name__=="__main__":
    sol = Solution()
    
    print(sol.isPrefixOfWord("i love eating burger", "burg"))
    print(sol.isPrefixOfWord("this problem is an easy problem", "pro"))
    print(sol.isPrefixOfWord("i am tired", "you"))