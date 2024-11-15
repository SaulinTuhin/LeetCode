from typing import List

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        N = len(arr)
        right = N - 1
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1
        res = right
        
        left = 0
        while left < right:
            while right < N and arr[left] > arr[right]:
                right += 1
            res = min(res, right - left - 1)
            if arr[left] > arr[left + 1]:
                break
            left += 1
        return res


if __name__=="__main__":
    sol = Solution()
    
    print(sol.findLengthOfShortestSubarray([1,2,3,10,4,2,3,5]))
    print(sol.findLengthOfShortestSubarray([5,4,3,2,1]))
    print(sol.findLengthOfShortestSubarray([1,2,3]))