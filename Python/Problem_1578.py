from typing import List

# Problem - 1578: https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
# Python3 Solution!
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        first_baloon, result = 0 , 0

        for second_baloon in range(1, len(colors)):
            if colors[first_baloon] == colors[second_baloon]:
                if neededTime[first_baloon] < neededTime[second_baloon]:
                    result += neededTime[first_baloon]
                    first_baloon = second_baloon
                else:
                    result += neededTime[second_baloon]
            else:
                first_baloon = second_baloon

        return result


if __name__=="__main__":
    sol = Solution()

    print(sol.minCost("abaac", [1,2,3,4,5]))
    print(sol.minCost("abc", [1,2,3]))
    print(sol.minCost("aabaa", [1,2,3,4,1]))