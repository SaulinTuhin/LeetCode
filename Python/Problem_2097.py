from typing import List
from collections import defaultdict

# Problem - 2097. Valid Arrangement of Pairs
# Python3 Solution!
class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        adj_matrix = defaultdict(list)
        in_out_degree = defaultdict(int)
        
        for start, end in pairs:
            adj_matrix[start].append(end)
            in_out_degree[start] += 1
            in_out_degree[end] -= 1
        startNode = pairs[0][0]
        for n in adj_matrix:
            if in_out_degree[n] == 1:
                startNode = n
                break
        
        res = []
        def dfs(cur_n):
            while adj_matrix[cur_n]:
                next_n = adj_matrix[cur_n].pop()
                dfs(next_n)
                res.append((cur_n, next_n))
        dfs(startNode)
        return res[::-1]


if __name__=="__main__":
    sol = Solution()
    
    print(sol.validArrangement([[5,1],[4,5],[11,9],[9,4]]))
    print(sol.validArrangement([[1,3],[3,2],[2,1]]))
    print(sol.validArrangement([[1,2],[1,3],[2,1]]))