from typing import List

# Problem - 1497. Check If Array Pairs Are Divisible by k
# Python3 Solution!
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        rem_freq = [0] * k
        for num in arr:
            rem = num % k
            if rem < 0:     # Not needed in python
                rem += k
            rem_freq[rem] += 1

        if rem_freq[0] % 2 != 0:
            return False
        for i in range(1, k // 2 + 1):
            if rem_freq[i] != rem_freq[k -i]:
                return False
        return True


if __name__=='__main__':
    sol = Solution()

    print(sol.canArrange([1,2,3,4,5,10,6,7,8,9], 5))
    print(sol.canArrange([1,2,3,4,5,6], 7))
    print(sol.canArrange([1,2,3,4,5,10,6,7,8,9], 10))