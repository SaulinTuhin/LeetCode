#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Problem - 452: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
// C++ Solution!
class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        sort(points.begin(), points.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });

        int res = 1;
        int prev_end = points[0][1];

        for (int i = 1; i < points.size(); i++) {
            if (prev_end < points[i][0]) {
                res++;
                prev_end = points[i][1];
            }
            else {
                prev_end = min(prev_end, points[i][1]);
            }
        }

        return res;
    }
};

int main() {
    Solution sol;

    vector<vector<int>> input = { {10,16}, {2,8}, {1,6}, {7,12} };
    cout << sol.findMinArrowShots(input) << endl;

    input = { {1,2}, {3,4}, {5,6}, {7,8} };
    cout << sol.findMinArrowShots(input) << endl;

    input = { {1,2}, {2,3}, {3,4}, {4,5} };
    cout << sol.findMinArrowShots(input) << endl;

    return 0;
}