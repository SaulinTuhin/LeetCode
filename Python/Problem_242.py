from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

if __name__ == "__main__":
    sol = Solution()

    s1 = "anagram"
    t1 = "nagaram"
    s2 = "rat"
    t2 = "car"
    s3 = "aa"
    t3 = "bb"

    print(sol.isAnagram(s1, t1))
    print(sol.isAnagram(s2, t2))
    print(sol.isAnagram(s3, t3))
