from collections import Counter, defaultdict

class Solution:
    def isAnagram_0(self, s: str, t: str) -> bool:
        """
        Likely a good intuitive starting position
        -------------
        O(nlog n) -> Time
        O(n) -> Space: Python strings are immutable
        """
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))

        return s == t
    
    def isAnagram_1(self, s: str, t: str) -> bool:
        """
        O(n) -> Time
        O(1) -> Space: Because the frequency arrays are fixed size
        """
        if len(s) != len(t):
            return False

        s_freq, t_freq = [0] * 26, [0] * 26
        for i in range(len(s)):
            s_freq[ord(s[i]) - ord('a')] += 1
            t_freq[ord(t[i]) - ord('a')] += 1
        
        return tuple(s_freq) == tuple(t_freq)
    
    def isAnagram_2(self, s: str, t: str) -> bool:
        """
        O(n) -> Time
        O(k) -> Space: Though k is actually constant so O(1)
        """
        if len(s) != len(t):
            return False
        
        s_freq, t_freq = defaultdict(int), defaultdict(int)
        for i in range(len(s)):
            s_freq[s[i]] += 1
            t_freq[t[i]] += 1

        for chr, count in s_freq.items():
            if count != t_freq[chr]:
                 return False
        return True
    
    def isAnagram_3(self, s: str, t: str) -> bool:
        """
        Should take the worst time, but surprisingly is gets the best times on Leetcode!
        Likely due to the particular inputs in leetcode, plus CPython's str.count is very optimized.
        A good example of limitations of big-oh notations alone
        -----------------
        O(n^2) -> Time due to repeated count operations
        O(1) -> Space
        """
        if len(s) != len(t):
            return False
        
        for c in set(s):
            if s.count(c) != t.count(c):
                return False
        return True
    
    def isAnagram_4(self, s: str, t: str) -> bool:
        """
        O(n) -> Time
        O(k) -> Space
        """
        return Counter(s) == Counter(t)
        

if __name__=="__main__":
    sol = Solution()

    print(sol.isAnagram_1("anagram", "nagaram"))
    print(sol.isAnagram_1("rat", "car"))