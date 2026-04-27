from typing import List
from collections import defaultdict
import heapq

class Solution:
    def topKFrequent_0(self, nums: List[int], k: int) -> List[int]:
        """
        O(nlogn) -> Time
        O(n) -> Memory
        """
        freq_map = defaultdict(int)
        for n in nums:
            freq_map[n] += 1
        
        ans = []
        for n, c in sorted(freq_map.items(), key=lambda item:item[1], reverse=True):
            ans.append(n)
            k -= 1
            if k == 0:
                break
        return ans
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        O(logn) -> Time
        O(n) -> Memory
        """
        freq_map = defaultdict(int)
        for n in nums:
            freq_map[n] += 1
        
        hp = []
        for n, c in freq_map.items():
            heapq.heappush(hp, (c, n))
            if len(hp) > k:
                heapq.heappop(hp)
        
        return [t[1] for t in hp]


if __name__=="__main__":
    sol = Solution()

    print(sol.topKFrequent([1,1,1,2,2,3], 2))
    print(sol.topKFrequent([1], 1))
    print(sol.topKFrequent([1,2,1,2,1,2,3,1,3,2], 2))