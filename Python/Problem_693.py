# Problem - 693. Binary Number with Alternating Bits
# Python3 Solution!
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        lastBit = n % 2
        n //= 2
        while n > 0:
            if lastBit == n % 2: return False
            lastBit = n % 2
            n //= 2
        return True
        
        
if __name__=='__main__':
    sol = Solution()
    
    print(sol.hasAlternatingBits(5))
    print(sol.hasAlternatingBits(7))
    print(sol.hasAlternatingBits(11))