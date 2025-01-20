from typing import List

# Problem - 2661. First Completely Painted Row or Column
# Python3 Solution!
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        row_painted = [0] * m
        col_painted = [0] * n

        num_matrix_map = {}
        for i in range(m):
            for j in range(n):
                num_matrix_map[mat[i][j]] = (i, j)
        
        for i, num in enumerate(arr):
            r, c = num_matrix_map[num]
            row_painted[r] += 1
            col_painted[c] += 1
            if row_painted[r] == n or col_painted[c] == m:
                return i
        return -1


if __name__=="__main__":
    sol = Solution()
    
    print(sol.firstCompleteIndex([1,3,4,2], [[1,4],[2,3]]))
    print(sol.firstCompleteIndex([2,8,7,4,1,3,5,6,9], [[3,2,5],[1,4,6],[8,7,9]]))