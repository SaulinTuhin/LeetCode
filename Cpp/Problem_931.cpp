#include <iostream>
#include <vector>

using namespace std;

// Problem - 931: https://leetcode.com/problems/minimum-falling-path-sum/
// C++ Solution!
class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& matrix) {
        int n = matrix.size();

        for (int r = 1; r < n; r++) {
            for (int c = 0; c < n; c++) {
                matrix[r][c] += min({
                    matrix[r - 1][c],
                    c > 0 ? matrix[r - 1][c - 1] : INT_MAX,
                    c < n - 1 ? matrix[r - 1][c + 1] : INT_MAX
                }
                );
            }
        }

        return *min_element(matrix[n - 1].begin(), matrix[n - 1].end());
    }
};

int main() {
    Solution sol;

    vector<vector<int>> input = { {2,1,3},{6,5,4},{7,8,9} };
    cout << sol.minFallingPathSum(input) << endl;
    input = { {-19,57},{-40,-5} };
    cout << sol.minFallingPathSum(input) << endl;

    return 0;
}