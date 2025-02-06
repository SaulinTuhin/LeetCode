from typing import List, DefaultDict

# Problem - 1726. Tuple with Same Product
# Python3 Solution!
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_count = DefaultDict(int)
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                product_count[nums[i] * nums[j]] += 1
        
        res = 0
        for cnt in product_count.values():
            res += 8 * (cnt * (cnt - 1) // 2)
        return res


if __name__ == "__main__":
    sol = Solution()

    print(sol.tupleSameProduct([2, 3, 4, 6]))
    print(sol.tupleSameProduct([1, 2, 4, 5, 10]))