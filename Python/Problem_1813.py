# Problem - 1813. Sentence Similarity III
# Python3 Solution!
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1, s2 = sentence1.split(), sentence2.split()
        if len(s2) < len(s1): s1, s2 = s2, s1
        
        l = 0
        while l < len(s1) and s1[l] == s2[l]:
            l += 1
            
        r1, r2 = len(s1) - 1, len(s2) - 1
        while r1 >= l and r2 >= 0 and s1[r1] == s2[r2]:
            r1, r2 = r1 - 1, r2 - 1
            
        return l > r1
        
        
if __name__=="__main__":
    sol = Solution()
    
    print(sol.areSentencesSimilar("My name is Haley", "My Haley"))
    print(sol.areSentencesSimilar("of", "A lot of words"))
    print(sol.areSentencesSimilar("Eating right now", "Eating"))