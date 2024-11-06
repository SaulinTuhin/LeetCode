from typing import List

# Problem - 3011. Find if Array Can Be Sorted
# Python3 Solution!
class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        prev_max = -1
        cur_set_bits = bin(nums[0]).count('1')
        cur_min = cur_max = nums[0]
        
        for i in range(1, len(nums)):
            if cur_set_bits == bin(nums[i]).count('1'):
                cur_min = min(cur_min, nums[i])
                cur_max = max(cur_max, nums[i])
            else:
                if cur_min < prev_max:
                    return False
                prev_max = cur_max
                cur_set_bits = bin(nums[i]).count('1')
                cur_max = cur_min = nums[i]
        return not cur_min < prev_max


if __name__=="__main__":
    sol = Solution()
    
    print(sol.canSortArray([8,4,2,30,15]))
    print(sol.canSortArray([1,2,3,4,5]))
    print(sol.canSortArray([3,16,8,4,2]))