package Problem_1496;
import java.util.HashSet;

/* Problem - 1496: https://leetcode.com/problems/path-crossing/
 * Java Solution!
*/
class Solution {
    public boolean isPathCrossing(String path) {
        HashSet <int[]> prev_pos = new HashSet<int[]>();
        int x = 0, y = 0;
        
        prev_pos.add(new int[] {x, y});

        for (int i = 0; i < path.length(); i++) {
            switch (path.charAt(i)) {
                case 'N':
                    x++;
                    break;
                case 'S':
                    x--;
                    break;
                case 'E':
                    y++;
                    break;
                default:
                    y--;
                    break;
            }

            if (prev_pos.contains(new int[]{x, y})) {
                return true;
            }
            else {
                prev_pos.add(new int[] {x, y});
            }
        }
        
        return false;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.isPathCrossing("NES"));
        System.out.println(sol.isPathCrossing("NESWW"));
    }
}