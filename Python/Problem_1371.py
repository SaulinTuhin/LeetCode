# Problem - 1371: Find the Longest Substring Containing Vowels in Even Counts
# Python3 Solution!
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {
            'a': 1,
            'e': 2,
            'i': 4,
            'o': 8,
            'u': 16
        }
        res, mask = 0, 0
        mask_map = [-1] * 32
        for i, c in enumerate(s):
            mask = mask ^ vowels.get(c, 0)
            if mask_map[mask] != -1 or mask == 0:
                length = i - mask_map[mask]
                res = max(res, length)
            else:
                mask_map[mask] = i

        return res


if __name__=="__main__":
    sol = Solution()

    print(sol.findTheLongestSubstring("eleetminicoworoep"))
    print(sol.findTheLongestSubstring("leetcodeisgreat"))
    print(sol.findTheLongestSubstring("bcbcbc"))