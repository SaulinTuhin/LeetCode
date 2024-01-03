from typing import List

#   Problem - 2125: https://leetcode.com/problems/number-of-laser-beams-in-a-bank/
#   Python Solution!
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        lastRowCount = bank[0].count('1')
        res = 0

        for row in range(1, len(bank)):
            thisRowCount = bank[row].count('1')

            if thisRowCount:
                res += lastRowCount * thisRowCount
                lastRowCount = thisRowCount

        return res


if __name__=="__main__":
    sol = Solution()

    print(sol.numberOfBeams(["011001","000000","010100","001000"]))
    print(sol.numberOfBeams(["000","111","000"]))