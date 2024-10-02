from typing import List

# Problem - 1331. Rank Transform of an Array
# Python3 Solution!
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_set = sorted(set(arr))

        rank = {n: i + 1 for i, n in enumerate(sorted_set)}

        return [rank[n] for n in arr]


if __name__=='__main__':
    sol = Solution()

    print(sol.arrayRankTransform([40,10,20,30]))
    print(sol.arrayRankTransform([100,100,100]))
    print(sol.arrayRankTransform([37,12,28,9,100,56,80,5,12]))