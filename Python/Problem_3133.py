# Problem - 3133. Minimum Array End
# Python3 Solution!
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res = x
        mask_x = 1
        n -= 1
        
        while n:
            if x & mask_x == 0:
                res |= (n & 1) * mask_x
                n >>= 1
            mask_x <<= 1
            
        return res
        
        
if __name__=="__main__":
    sol = Solution()
    
    print(sol.minEnd(3, 4))
    print(sol.minEnd(2, 7))