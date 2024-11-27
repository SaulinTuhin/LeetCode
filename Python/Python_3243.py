from typing import List
from collections import deque

# Problem - 3243. Shortest Distance After Road Addition Queries I
# Python3 Solution!
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        res = []
        dist_adj_map = [[i, [i + 1]] for i in range(n)]
        dist_adj_map[-1][1][0] = -1

        for u, v in queries:
            dist_adj_map[u][1].append(v)
            if dist_adj_map[v][0] > dist_adj_map[u][0]:
                queue = deque([u])
                while queue:
                    cur = queue.popleft()
                    for next in dist_adj_map[cur][1]:
                        if next > -1 and dist_adj_map[next][0] > dist_adj_map[cur][0] + 1:
                            dist_adj_map[next][0] = dist_adj_map[cur][0] + 1
                            queue.append(next)
            res.append(dist_adj_map[-1][0])
        return res
    

if __name__=="__main__":
    sol = Solution()
    
    print(sol.shortestDistanceAfterQueries(5, [[2,4],[0,2],[0,4]]))
    print(sol.shortestDistanceAfterQueries(4, [[0,3],[0,2]]))