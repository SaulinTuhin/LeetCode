from math import ceil
from typing import List

# Problem - 1760. Minimum Limit of Balls in a Bag
# Python3 Solution!
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        total = sum(nums)
        max_length = len(nums) + maxOperations
        low, high = ceil(total / max_length), min(max(nums), total // maxOperations)
        
        def is_possible(operationLimit: int):
            operation_count = 0
            for num in nums:
                operation_count += ceil(num / operationLimit) - 1
                if operation_count > maxOperations:
                    return False
            return True
        
        while low < high:
            mid = (high + low) // 2
            if is_possible(mid):
                high = mid
            else:
                low = mid + 1
        return low


if __name__=="__main__":
    sol = Solution()
    
    print(sol.minimumSize([9], 2))
    print(sol.minimumSize([2,4,8,2], 4))