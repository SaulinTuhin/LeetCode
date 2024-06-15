import heapq
from typing import List

# Problem - 502: https://leetcode.com/problems/ipo/
# Python3 Solution!
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxProfit = []
        minCapital = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(minCapital)

        for i in range(k):
            while minCapital and minCapital[0][0] <= w:
                c, p = heapq.heappop(minCapital)
                heapq.heappush(maxProfit, -p)

            if not maxProfit:
                break

            w -= heapq.heappop(maxProfit)
        return w
        

if __name__=="__main__":
    sol = Solution()

    print(sol.findMaximizedCapital(2, 0, [1,2,3], [0,1,1]))
    print(sol.findMaximizedCapital(3, 0, [1,2,3], [0,1,2]))