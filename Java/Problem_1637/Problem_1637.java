import java.util.Arrays;

class Solution {
    public int maxWidthOfVerticalArea(int[][] points) {
        Arrays.sort(points, (a, b) -> Integer.compare(a[0], b[0]));

        int max_gap = 0;
        for (int i = 0; i < points.length - 1; i++){
            max_gap = Math.max(max_gap, points[i+1][0] - points[i][0]);
        }

        return max_gap;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.maxWidthOfVerticalArea(new int[][]{{8, 7},{9, 9},{7, 4},{9, 7}}));
        System.out.println(sol.maxWidthOfVerticalArea(new int[][]{{3, 1},{9, 0},{1, 0},{1, 4},{5, 3},{8, 8}}));
    }
}