from typing import DefaultDict, List

#   Problem - 2610: https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/
#   Python Solution!
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        numCount = DefaultDict(int)
        res = []

        for num in nums:
            row = numCount[num]

            if row == len(res):
                res.append([])

            res[row].append(num)
            numCount[num] += 1

        return res
    

if __name__=="__main__":
    sol = Solution()

    print(sol.findMatrix([1,3,4,1,2,3,1]))
    print(sol.findMatrix([1,2,3,4]))
    print(sol.findMatrix([2,1,1]))