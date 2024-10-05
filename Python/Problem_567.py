# Problem - 567. Permutation in String
# Python3 Solution!
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        s1Freq = [0] * 26
        s2Freq = [0] * 26
        for i in range(len(s1)):
            s1Freq[ord(s1[i]) - ord('a')] += 1
            s2Freq[ord(s2[i]) - ord('a')] += 1
            
        matchCount = 0
        for i in range(26):
            matchCount += 1 if s1Freq[i] == s2Freq[i] else 0
            
        left = 0
        for right in range(len(s1), len(s2)):
            if matchCount == 26: return True
            
            idx = ord(s2[left]) - ord('a')
            s2Freq[idx] -= 1
            if s1Freq[idx] == s2Freq[idx]:
                matchCount += 1
            elif s1Freq[idx] - 1 == s2Freq[idx]:
                matchCount -= 1
            left += 1
            
            idx = ord(s2[right]) - ord('a')
            s2Freq[idx] += 1
            if s1Freq[idx] == s2Freq[idx]:
                matchCount += 1
            elif s1Freq[idx] + 1 == s2Freq[idx]:
                matchCount -= 1
        return matchCount == 26


if __name__=="__main__":
    sol = Solution()

    print(sol.checkInclusion("ab", "eidbaooo"))
    print(sol.checkInclusion("ab", "eidboaoo"))