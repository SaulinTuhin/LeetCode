from typing import List
from collections import deque
import heapq

# Problem - 2290. Minimum Obstacle Removal to Reach Corner
# Python3 Solution!
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        adjecent = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        ]
        min_heap = deque([(grid[0][0], 0, 0)])
        visited = [[False] * n for _ in grid]
        while min_heap:
            cur_cost, x, y = min_heap.popleft()

            if x == m - 1 and y == n - 1:
                return cur_cost
            for i, j in adjecent:
                xn, yn = x + i, y + j
                if 0 <= xn < m and 0 <= yn < n and not visited[xn][yn]:
                    if grid[xn][yn] == 0:
                        min_heap.appendleft((cur_cost, xn, yn))
                    else:
                        min_heap.append((cur_cost + grid[xn][yn], xn, yn))
                    visited[xn][yn] = True
        return -1
    
    
    def minimumObstacles_heap(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        adjecent = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0]
        ]

        min_heap = [(grid[0][0], 0, 0)]
        visited = {(0, 0)}
        while min_heap:
            cur_cost, x, y = heapq.heappop(min_heap)
            if x == m - 1 and y == n - 1:
                return cur_cost
            for i, j in adjecent:
                xn, yn = x + i, y + j
                if xn >= 0 and xn < m and yn >= 0 and yn < n and (xn, yn) not in visited:
                    heapq.heappush(min_heap, (cur_cost + grid[xn][yn], xn, yn))
                    visited.add((xn, yn))
        return -1



if __name__=="__main__":
    sol = Solution()
    
    print(sol.minimumObstacles([[0,1,1],[1,1,0],[1,1,0]]))
    print(sol.minimumObstacles([[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]))