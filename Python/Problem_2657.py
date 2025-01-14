from typing import List

# Problem - 2657. Find the Prefix Common Array of Two Arrays
# Python3 Solution!
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        member_set = set()
        res =  []
        cur_common = 0
        for n1, n2 in zip(A, B):
            if n1 in member_set:
                cur_common += 1
            else:
                member_set.add(n1)
            if n2 in member_set:
                cur_common += 1
            else:
                member_set.add(n2)
            res.append(cur_common)
        return res


if __name__=="__main__":
    sol = Solution()
    
    print(sol.findThePrefixCommonArray([1,3,2,4], [3,1,2,4]))
    print(sol.findThePrefixCommonArray([2,3,1], [3,1,2]))