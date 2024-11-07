from typing import List

# Problem - 2275. Largest Combination With Bitwise AND Greater Than Zero
# Python3 Solution!
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        res = 0
        for i in range(24):
            cur_count = 0
            for c in candidates:
                if c & (1 << i):
                    cur_count += 1
            res = max(res, cur_count)
        return res


if __name__=="__main__":
    sol = Solution()
    
    print(sol.largestCombination([16,17,71,62,12,24,14]))
    print(sol.largestCombination([8,8]))