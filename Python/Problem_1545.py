# Problem - 1545. Find Kth Bit in Nth Binary String
# Python3 Solution!
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        length = 2 ** n - 1
        
        def rec(length: int, k: int) -> str:
            if length == 1:
                return '0'
            
            mid = length // 2
            
            if k == mid + 1:
                return '1'
            elif k <= mid:
                return rec(mid, k)
            else:
                res = rec(mid, 1 + length - k)
                return '0' if res == '1' else '1'
        
        return rec(length, k)
    
    def findKthBit_linear(self, n: int, k: int) -> str:
        length = 2 ** n - 1
        inverse = False
        while (k > 1):
            mid = length // 2
            
            if k == mid + 1:
                return '0' if inverse else '1'
            elif k <= mid:
                length = mid
            else:
                k = 1 + length - k
                length = mid
                inverse = not inverse
        
        return '1' if inverse else '0'
        
        
if __name__=="__main__":
    sol = Solution()
    
    print(sol.findKthBit(3, 1))
    print(sol.findKthBit(4, 11))
    print(sol.findKthBit(3, 5))
    
    print('')
    
    print(sol.findKthBit_linear(3, 1))
    print(sol.findKthBit_linear(4, 11))
    print(sol.findKthBit_linear(3, 5))