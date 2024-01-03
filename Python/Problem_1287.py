from typing import List

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        tarCount = len (arr) // 4

        prev = None
        for i in range(len(arr) - tarCount):
            if i == prev:
                continue
            prev = i

            if arr[i] == arr[i + tarCount]:
                return arr[i]


if __name__ == "__main__":
    solution = Solution()

    input1 = [1,2,2,6,6,6,6,7,10]
    input2 = [1,2,3,3]
    output = solution.findSpecialInteger(input1)

    print(output)