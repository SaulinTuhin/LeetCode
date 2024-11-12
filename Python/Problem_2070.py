from typing import List
from bisect import bisect

# Problem - 2070. Most Beautiful Item for Each Query
# Python3 Solution!
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda x: x[0])
        for i in range(1, len(items)):
            items[i][1] = max(items[i - 1][1], items[i][1])

        res = []
        for q in queries:
            idx = bisect(items, q, key= lambda items:items[0]) - 1
            if idx < 0 or items[idx][0] > q:
                res.append(0)
            else:
                res.append(items[idx][1])
        return res


if __name__=="__main__":
    sol = Solution()
    
    print(sol.maximumBeauty([[1,2],[3,2],[2,4],[5,6],[3,5]], [1,2,3,4,5,6]))
    print(sol.maximumBeauty([[1,2],[1,2],[1,3],[1,4]], [1]))
    print(sol.maximumBeauty([[10,1000]], [5]))