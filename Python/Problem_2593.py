from typing import List
import heapq

class Solution:
    def findScore(self, nums: List[int]) -> int:
        heap = [(n, i) for i, n in enumerate(nums)]
        marked = set()
        heapq.heapify(heap)

        res = 0
        while heap:
            cur, idx = heapq.heappop(heap)
            if idx in marked:
                continue
            res += cur
            marked.add(idx)
            marked.add(idx - 1)
            marked.add (idx + 1)
        return res


if __name__=="__main__":
    sol = Solution()
    
    print(sol.findScore([2,1,3,4,5,2]))
    print(sol.findScore([2,3,5,1,3,2]))