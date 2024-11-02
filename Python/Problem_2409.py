# Problem - 2490. Circular Sentence
# Python3 Solution!
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]:
            return False
        
        for i in range(len(sentence)):
            if sentence[i] != ' ':
                continue
            if sentence[i - 1] != sentence[i + 1]:
                return False
        return True
    
    def isCircularSentence_split(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]:
            return False
        sentence = sentence.split(' ')
        
        for i in range(1, len(sentence)):
            if sentence[i][0] != sentence[i - 1][-1]:
                return False
        return True


if __name__=="__main__":
    sol = Solution()
    
    print(sol.isCircularSentence("leetcode exercises sound delightful"))
    print(sol.isCircularSentence("eetcode"))
    print(sol.isCircularSentence("Leetcode is cool"))