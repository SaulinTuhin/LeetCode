#include <iostream>

using namespace std;

// Problem - 70: https://leetcode.com/problems/climbing-stairs/
// C++ Solution!
class Solution {
public:
    int climbStairs(int n) {
        int prev = 1, prev_prev = 1;
        for (int i = 1; i < n; i++) {
            int temp = prev;
            prev += prev_prev;
            prev_prev = temp;
        }

        return prev;
    }
};

int main() {
    Solution sol;

    cout << sol.climbStairs(2) << endl;
    cout << sol.climbStairs(3) << endl;
    cout << sol.climbStairs(5) << endl;

    return 0;
}