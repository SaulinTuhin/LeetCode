# Problem - 762. Prime Number of Set Bits in Binary Representation
# Python3 Solution!
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        res = 0
        for n in range(left, right + 1):
            if n.bit_count() in {2, 3, 5, 7, 11, 13, 17, 19}:
                res += 1
        return res


if __name__=="__main__":
    sol = Solution()
    
    print(sol.countPrimeSetBits(6, 10))
    print(sol.countPrimeSetBits(10, 15))