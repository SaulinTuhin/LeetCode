from typing import List

# Observations -
# 1. We want to know the number of moves possible from any given (row, col) position.
# 2. Same (row, col) will be visited from multiple other cells, meaning repeat work. So we can use Dynamic Programming.
# Approach -
# 1. Starting from (0, 0) traverse every valid cell in the given directions.
#   1.1. For each valid next cell, increment count by 1.
#   1.2. Cur cell's count will be max count of all valid adjacent cells.
#   1.3. Run this for all cells in first col.

# Problem - 2684. Maximum Number of Moves in a Grid
# Python3 Solution!
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        cache = {}
        def dfs(row, col):
            if (row, col) in cache:
                return cache[(row, col)]
            
            count = 0
            for r, c in [(row - 1, col + 1), (row, col + 1), (row + 1, col + 1)]:
                if 0 <= r < ROW and c < COL and grid[r][c] > grid[row][col]:
                    count = max(count, 1 + dfs(r, c))
            cache[(row, col)] = count
            return cache[(row, col)]
        
        res = 0
        for r in range(ROW):
            res = max(res, dfs(r, 0))
        return res
    
    
if __name__=="__main__":
    sol = Solution()
    
    print(sol.maxMoves([[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]))
    print(sol.maxMoves([[3,2,4],[2,1,9],[1,1,7]]))