from typing import List

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()

        max_gap = 0
        for i in range(len(points) - 1):
            max_gap = max(points[i+1][0] - points[i][0], max_gap)

        return max_gap


if __name__=="__main__":
    sol = Solution()

    print(sol.maxWidthOfVerticalArea([[8,7],[9,9],[7,4],[9,7]]))
    print(sol.maxWidthOfVerticalArea([[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]))