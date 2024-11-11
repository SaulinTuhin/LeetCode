from typing import List
import math

# Problem - 2601. Prime Subtraction Operation
# Python3 Solution!
class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        max_element = max(nums)
        is_prime = [True] * (max_element + 1)
        is_prime[1] = 0
        for i in range(2, int(math.sqrt(max_element + 1)) + 1):
            if is_prime:
                for j in range(i *i, max_element + 1, i):
                    is_prime[j] = False
        
        best_value = 1
        i = 0
        while i < len(nums):
            diff = nums[i] - best_value
            if diff < 0:
                return False
            
            if is_prime[diff] or not diff:
                i += 1
                best_value += 1
            else:
                best_value += 1
        return True


if __name__=="__main__":
    sol = Solution()
    
    print(sol.primeSubOperation([4,9,6,10]))
    print(sol.primeSubOperation([6,8,11,12]))
    print(sol.primeSubOperation([5,8,3]))