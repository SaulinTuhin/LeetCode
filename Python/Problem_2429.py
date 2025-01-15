# Problem - 2429. Minimize XOR
# Python3 Solution!
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        res = num1
        target_cnt = bin(num2).count("1")
        cur_cnt = bin(res).count("1")
        bit_pointer = 0
        
        while cur_cnt < target_cnt:
            if (res & (1 << bit_pointer)) == 0:
                res = res | (1 << bit_pointer)
                cur_cnt += 1
            bit_pointer += 1
        while cur_cnt > target_cnt:
            if (res & (1 << bit_pointer)) != 0:
                res = res & ~(1 << bit_pointer)
                cur_cnt -= 1
            bit_pointer += 1
        return res


if __name__=="__main__":
    sol = Solution()
    
    print(sol.minimizeXor(3, 5))
    print(sol.minimizeXor(1, 12))
    print(sol.minimizeXor(79, 74))