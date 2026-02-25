from typing import List

# Problem - 1356. Sort Integers by The Number of 1 Bits
# Python3 Solution!
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def countSetBits(num):
            count = 0
            while num:
                count += 1
                num &= (num - 1)
            return count
        
        arr.sort(key = lambda num: (countSetBits(num), num))
        return arr


if __name__=="__main__":
    sol = Solution()

    print(sol.sortByBits([0,1,2,3,4,5,6,7,8]))
    print(sol.sortByBits([1024,512,256,128,64,32,16,8,4,2,1]))