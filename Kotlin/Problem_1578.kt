// Problem - 1578: https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
// Kotlin Solution!
class Solution {
    fun minCost(colors: String, neededTime: IntArray): Int {
        var first_baloon = 0;
        var result = 0;

        for (second_baloon in 1..<colors.length) {
            if (colors[first_baloon] == colors[second_baloon]){
                if (neededTime[first_baloon] < neededTime[second_baloon]){
                    result += neededTime[first_baloon];
                    first_baloon = second_baloon;
                }
                else {
                    result += neededTime[second_baloon];
                }
            }
            else {
                first_baloon = second_baloon;
            }
        }

        return result;
    }
}

fun main() {
    var sol = Solution();

    println(sol.minCost("abaac", intArrayOf(1,2,3,4,5)));
    println(sol.minCost("abc", intArrayOf(1,2,3)));
    println(sol.minCost("aabaa", intArrayOf(1,2,3,4,1)));
}