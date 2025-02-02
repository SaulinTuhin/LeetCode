from typing import List

# Problem - 1752. Check if Array Is Sorted and Rotated
# Python3 Solution!
class Solution:
    def check(self, nums: List[int]) -> bool:
        N = len(nums)
        
        cur_length = 1
        for i in range(1, 2 * N):
            if nums[(i - 1) % N] <= nums[i % N]:
                cur_length += 1
            else:
                cur_length = 1
            if cur_length == N:
                return True
        return N == 1


if __name__=="__main__":
    sol = Solution()
    
    print(sol.check([3,4,5,1,2]))
    print(sol.check([2,1,3,4]))
    print(sol.check([1,2,3]))