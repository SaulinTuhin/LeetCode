from collections import defaultdict, Counter

# Problem - 2981. Find Longest Special Substring That Occurs Thrice I
# Python3 Solution!
class Solution:
    def maximumLength(self, s: str) -> int:
        substring_map = defaultdict(int)
        res = -1
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                cur_sub = s[i:j]
                substring_map[cur_sub] += 1
                if substring_map[cur_sub] >= 3 and len(cur_sub) > res and len(Counter(cur_sub)) == 1:
                    res = len(cur_sub)
        return res


if __name__=="__main__":
    sol = Solution()
    
    print(sol.maximumLength("aaaa"))
    print(sol.maximumLength("abcdef"))
    print(sol.maximumLength("abcaba"))