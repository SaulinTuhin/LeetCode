from typing import List

# Problem - 1652. Defuse the Bomb
# Python3 Solution!
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0: return [0] * len(code)

        res = []
        n = len(code)
        left, right, cur_sum = 1, k, 0
        if k < 0:
            left = n - abs(k)
            right = n - 1
        
        for i in range(left, right + 1):
            cur_sum += code[i]
        
        for i in range(n):
            res.append(cur_sum)
            cur_sum -= code[left]
            left = (left + 1) % n
            right = (right + 1) % n
            cur_sum += code[right]
        return res
    
    def decrypt_pythonic(self, code: List[int], k: int) -> List[int]:
        tmp = 2 * code
        n = len(code)
        if k == 0: return [0] * n
        elif k > 0: return [sum(tmp[i+1 : i+1+k]) for i in range(n)]
        else: return [sum(tmp[i+n+k: i+n]) for i in range(n)]


if __name__=="__main__":
    sol = Solution()
    
    print(sol.decrypt([5,7,1,4], 3))
    print(sol.decrypt([1,2,3,4], 0))
    print(sol.decrypt([2,4,9,3], -2))