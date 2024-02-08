#include <iostream>
#include <vector>

using namespace std;

// Problem - 279: https://leetcode.com/problems/perfect-squares/
// C++ Solution!
class Solution {
public:
    int numSquares(int n) {
        vector<int> dp(n + 1, n);
        dp[0] = 0;

        for (int remainingTarget = 1; remainingTarget <= n; remainingTarget++) {
            for (int i = 1; i <= n; i++) {
                int square = i * i;
                if (remainingTarget - square < 0)
                    break;
                dp[remainingTarget] = min(dp[remainingTarget], 1 + dp[remainingTarget - square]);
            }
        }

        return dp[n];
    }
};

int main() {
    Solution sol;

    cout << sol.numSquares(12) << endl;
    cout << sol.numSquares(13) << endl;

    return 0;
}