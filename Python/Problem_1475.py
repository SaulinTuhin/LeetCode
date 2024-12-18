from typing import List

# Problem - 1475. Final Prices With a Special Discount in a Shop
# Python3 Solution!
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                prices[stack.pop()] -= prices[i]
            stack.append(i)

        return prices


if __name__=="__main__":
    sol = Solution()
    
    print(sol.finalPrices([8,4,6,2,3]))
    print(sol.finalPrices([1,2,3,4,5]))
    print(sol.finalPrices([10,1,1,6]))