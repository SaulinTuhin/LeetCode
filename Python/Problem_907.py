from typing import List

# Problem - 907: https://leetcode.com/problems/sum-of-subarray-minimums/
# Python3 Solution!
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        res = 0
        stack = []

        for i, n in enumerate(arr):
            while stack and n < stack[-1][1]:
                j, m = stack.pop()
                left = j - stack[-1][0] if stack else j + 1
                right = i - j
                res = (res + m * left * right) % MOD
            stack.append((i, n))

        for i in range(len(stack)):
            j, n = stack[i]
            left = j - stack[i - 1][0] if i > 0 else j + 1
            right = len(arr) - j
            res = (res + n * left * right) % MOD

        return res
    

if __name__=='__main__':
    sol = Solution()

    print(sol.sumSubarrayMins([3,1,2,4]))
    print(sol.sumSubarrayMins([11,81,94,43,3]))