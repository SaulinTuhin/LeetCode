// Problem - 1614: Maximum Nesting Depth of the Parentheses
// Java Solution!
class Solution {
    public int maxDepth(String s) {
        int res = 0, curDepth = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(')
                curDepth++;
            else if (s.charAt(i) == ')')
                curDepth--;

            res = Math.max(curDepth, res);
        }

        return res;
    }
}

public static void main(String[] args) {
    Solution sol = new Solution();

    System.out.println(sol.maxDepth("(1+(2*3)+((8)/4))+1"));
    System.out.println(sol.maxDepth("(1)+((2))+(((3)))"));
}