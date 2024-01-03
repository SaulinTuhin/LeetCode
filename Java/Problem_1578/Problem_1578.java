package Java.Problem_1578;
/* 
* Problem - 1578: https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
* Java Solution!
*/
class Solution {
    public int minCost(String colors, int[] neededTime) {
        int first_baloon = 0, result = 0;

        for (int second_baloon = 1; second_baloon < colors.length(); second_baloon++){
            if (colors.charAt(first_baloon) == colors.charAt(second_baloon)) {
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

    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.minCost("abaac", new int[] {1,2,3,4,5}));
        System.out.println(sol.minCost("abc", new int[] {1,2,3}));
        System.out.println(sol.minCost("aabaa", new int[] {1,2,3,4,1}));
    }
}