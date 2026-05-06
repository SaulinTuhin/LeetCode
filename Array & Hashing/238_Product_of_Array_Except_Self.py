from typing import List

class Solution:
    def productExceptSelf_0(self, nums: List[int]) -> List[int]:
        """
        Gets TLE on Leetcode, because O(n) time requirement was mentioned explicitly.
        If this is not mentioned during interview I would consider starting here.
        O(n^2) -> Time
        O(1) -> Space (Because description says output array is not considered extra space).
        """
        res = [0] * len(nums)
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                product *= nums[j]
            res[i] = product
        return res
    
    def productExceptSelf_1(self, nums: List[int]) -> List[int]:
        """
        O(n) -> Time
        O(n) -> Space
        """
        n = len(nums)
        res = [0] * n
        prefix_product, postfix_product = [0] * n, [0] * n
        forward_product, reverse_product = 1, 1
        for i in range(n):
            j = n - i - 1
            prefix_product[i] = forward_product
            forward_product *= nums[i]
            postfix_product[j] = reverse_product
            reverse_product *= nums[j]

        for i in range(len(nums)):
            res[i] = prefix_product[i] * postfix_product[i]
        return res
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        O(n) -> Time
        O(1) -> Space
        """
        n = len(nums)
        res = [1] * n
        pre_product, post_product = 1, 1
        for i in range(n):
            j = n - i - 1
            res[i] *= pre_product
            res[j] *= post_product
            pre_product *= nums[i]
            post_product *= nums[j]
        return res


if __name__=="__main__":
    sol = Solution()

    print(sol.productExceptSelf([1,2,3,4]))
    print(sol.productExceptSelf([-1,1,0,-3,3]))