from typing import List

# Problem - 3152. Special Array II
# Python3 Solution!
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        non_parity_map = [0] * len(nums)
        cur_parity_count = 0
        prev_parity = nums[0] % 2
        for i in range(1, len(nums)):
            if nums[i] % 2 == prev_parity:
                cur_parity_count += 1
            prev_parity = nums[i] % 2
            non_parity_map[i] = cur_parity_count
        
        res = []
        for start, end in queries:
            res.append(non_parity_map[end] - non_parity_map[start] == 0)
        return res


if __name__=="__main__":
    sol = Solution()
    
    print(sol.isArraySpecial([3,4,1,2,6], [[0,4]]))
    print(sol.isArraySpecial([4,3,1,6], [[0,2],[2,3]]))