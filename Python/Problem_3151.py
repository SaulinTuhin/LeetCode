from typing import List

# Problem - 3151. Special Array I
# Python3 Solution!
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        prev_parity = nums[0] % 2
        for i in range(1, len(nums)):
            cur_parity = nums[i] % 2
            if cur_parity != prev_parity:
                prev_parity = cur_parity
                continue
            else:
                return False
        return True


if __name__=="__main__":
    sol = Solution()
    
    print(sol.isArraySpecial([1]))
    print(sol.isArraySpecial([2,1,4]))
    print(sol.isArraySpecial([4,3,1,6]))