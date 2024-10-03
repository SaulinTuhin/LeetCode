from typing import List

# Problem - 1590. Make Sum Divisible by P
# Python3 Solution!
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        rem = total % p

        if rem == 0:
            return 0
        
        res = len(nums)
        cur_rem = 0
        rem_map = {0:-1}
        for i, n in enumerate(nums):
            cur_rem = (cur_rem + n) % p
            prefix_to_remove = (cur_rem - rem + p) % p
            if prefix_to_remove in rem_map:
                length = i - rem_map[prefix_to_remove]
                res = min(length, res)
            rem_map[cur_rem] = i

        return -1 if res == len(nums) else res


if __name__=='__main__':
    sol = Solution()

    print(sol.minSubarray([3,1,4,2], 6))
    print(sol.minSubarray([6,3,5,2], 9))
    print(sol.minSubarray([1,2,3], 3))