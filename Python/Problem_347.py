from typing import List
from collections import Counter

# Problem - 347. Top K Frequent Elements
# Python3 Solution!
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        return [k for k, _ in sorted(freq_map.items(), key=lambda item: item[1], reverse=True)][:k]


if __name__=="__main__":
    sol = Solution()
    
    print(sol.topKFrequent([1,1,1,2,2,3], 2))
    print(sol.topKFrequent([1], 1))