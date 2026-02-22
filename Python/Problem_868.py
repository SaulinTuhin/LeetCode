# Problem - 868. Binary Gap
# Python3 Solution!
class Solution:
    def binaryGap(self, n: int) -> int:
        last_i = -1
        res = 0
        for i in range(32):
            if n % 2 == 1:
                if last_i != -1:
                    res = max(res, i - last_i)
                last_i = i
            n //= 2
        return res
    
    def binaryGap_shiftR(self, n: int) -> int:
        last_i = -1
        res = 0
        for i in range(32):
            if (n >> i) & 1:
                if last_i >= 0 and i - last_i > res:
                    res = i - last_i
                last_i = i
        return res


if __name__=="__main__":
    sol = Solution()

    print(sol.binaryGap(22))
    print(sol.binaryGap(8))
    print(sol.binaryGap(5))