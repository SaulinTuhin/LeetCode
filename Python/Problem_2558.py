from typing import List
import heapq
from math import floor

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-g for g in gifts]
        heapq.heapify(gifts)
        while k > 0:
            cur = -heapq.heappop(gifts)
            left = floor(cur ** 0.5)
            heapq.heappush(gifts, -left)
            k -= 1
        return -sum(gifts)


if __name__=="__main__":
    sol = Solution()
    
    print(sol.pickGifts([25,64,9,4,100], 4))
    print(sol.pickGifts([1,1,1,1], 4))