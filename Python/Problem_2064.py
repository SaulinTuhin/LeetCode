from typing import List
from math import ceil

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        if n == len(quantities): return max(quantities)
        
        total_products = sum(quantities)
        left, right = total_products // n, max(quantities)
        
        def is_possible(x):
            shop_count = 0
            for q in quantities:
                if q > x:
                    shop_count += ceil(q / x)
                else:
                    shop_count += 1
            return shop_count <= n and shop_count <= total_products
        
        while left < right:
            mid = (left + right) // 2
            if mid and is_possible(mid):
                right = mid
            else:
                left = mid + 1
        return left
            
    
    def minimizedMaximum_1(self, n: int, quantities: List[int]) -> int:
        right = max(quantities)
        if n == len(quantities): return right
        
        total_products = sum(quantities)
        left = total_products // n

        def is_possible(x):
            cur_product = 0
            cur_remaining = quantities[cur_product]

            for shop in range(n):
                if cur_remaining > x:
                    cur_remaining -= x
                else:
                    if cur_product == len(quantities) - 1:
                        return True
                    cur_product += 1
                    cur_remaining = quantities[cur_product]
            return False

        while left < right:
            mid = left + (right - left) // 2
            if is_possible(mid):
                right = mid
            else:
                left = mid + 1
        return left


if __name__=="__main__":
    sol = Solution()
    
    print(sol.minimizedMaximum(6, [11,6])) 
    print(sol.minimizedMaximum(7, [15,10,10])) 
    print(sol.minimizedMaximum(1, [100000]))
    print(sol.minimizedMaximum(2, [1, 10000]))