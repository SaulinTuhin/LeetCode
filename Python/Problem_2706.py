from typing import List

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min, second_min = 101, 101

        for price in prices:
            if price < min:
                second_min = min
                min = price
            elif price < second_min:
                second_min = price

        return (money - min - second_min) if (money - min - second_min >= 0) else money


if __name__=="__main__":
    sol = Solution()

    print(sol.buyChoco([1,2,2], 3))
    print(sol.buyChoco([3,2,3], 3))
