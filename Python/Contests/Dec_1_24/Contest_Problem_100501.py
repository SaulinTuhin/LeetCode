class Solution:
    def smallestNumber(self, n: int) -> int:
        bit_count = len(bin(n)[2:])
        res = 1 << bit_count
        return res - 1


if __name__=="__main__":
    sol = Solution()
    
    print(sol.smallestNumber(5))
    print(sol.smallestNumber(10))
    print(sol.smallestNumber(3))