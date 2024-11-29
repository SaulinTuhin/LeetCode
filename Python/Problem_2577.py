from typing import List
import heapq

# Problem - 2577. Minimum Time to Visit a Cell In a Grid
# Python3 Solution!
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1: return -1
        rows, cols = len(grid), len(grid[0])
        adjecent = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        visited = [[False] * cols for _ in grid]
        pq = [(grid[0][0], 0, 0)]
        visited[0][0] = True
        while pq:
            cur_time, x, y = heapq.heappop(pq)
            if x == rows - 1 and y == cols - 1:
                return cur_time
            
            for i, j in adjecent:
                xn, yn = x + i, y + j
                if 0 <= xn < rows and 0 <= yn < cols and not visited[xn][yn]:
                    if cur_time + 1 > grid[xn][yn]:
                        heapq.heappush(pq, (cur_time + 1, xn, yn))
                    else:
                        wait_time = 1 if (grid[xn][yn] - cur_time) % 2 == 0 else 0
                        heapq.heappush(pq, (grid[xn][yn] + wait_time, xn, yn))
                    visited[xn][yn] = True
        return -1


if __name__=="__main__":
    sol = Solution()
    
    print(sol.minimumTime([[0,1,3,2],[5,1,2,5],[4,3,8,6]]))
    print(sol.minimumTime([[0,2,4],[3,2,1],[1,0,4]]))