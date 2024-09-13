from typing import List

# Problem - 1310: XOR Queries of a Subarray
# Python3 Solution!
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix_xor = [0]
        for i in arr:
            prefix_xor.append(prefix_xor[-1] ^ i)

        res = []
        for l, r in queries:
            res.append(prefix_xor[r+1]^prefix_xor[l])

        return res
    

if __name__=="__main__":
    sol = Solution()

    res = sol.xorQueries([1,3,4,8], [[0,1],[1,2],[0,3],[3,3]])
    for i in res:
        print(i, end=' ')
    print('')

    res = sol.xorQueries([4,8,2,10], [[2,3],[1,3],[0,0],[0,3]])
    for i in res:
        print(i, end=' ')
    print('')