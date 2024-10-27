from collections import defaultdict
from typing import List

# Problem - 1277. Count Square Submatrices with All Ones
# Python3 Solution!
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ROW, COL = len(matrix), len(matrix[0])
        dp = defaultdict(int)
        res = 0
        for r in range(ROW):
            cur_dp = defaultdict(int)
            for c in range(COL):
                if matrix[r][c]:
                    cur_dp[c] = 1 + min(
                        dp[c],
                        cur_dp[c - 1],
                        dp[c - 1]
                    )
                    res += cur_dp[c]
            dp = cur_dp
        return res
    
    def countSquares_recursive(self, matrix: List[List[int]]) -> int:
        ROW, COL = len(matrix), len(matrix[0])
        cache = {}
        def dfs(r, c):
            if r == ROW or c == COL or not matrix[r][c]:
                return 0
            if (r, c) in cache:
                return cache[(r, c)]
            cache[(r, c)] = 1 + min (
                dfs(r + 1, c),
                dfs(r, c + 1),
                dfs(r + 1, c + 1)
            )
            return cache[(r, c)]    
        res = 0
        for r in range(ROW):
            for c in range(COL):
                res += dfs(r, c)
        return res
        
        
if __name__=="__main__":
    sol = Solution()
    
    print(sol.countSquares([[0,1,1,1],[1,1,1,1],[0,1,1,1]]))
    print(sol.countSquares([[1,0,1],[1,1,0],[1,1,0]]))
    
    print("-----Recursive-----")
    print(sol.countSquares_recursive([[0,1,1,1],[1,1,1,1],[0,1,1,1]]))
    print(sol.countSquares_recursive([[1,0,1],[1,1,0],[1,1,0]]))