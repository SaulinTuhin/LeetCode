#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Problem - 368: https://leetcode.com/problems/largest-divisible-subset/
// C++ Solution!
class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        sort(nums.begin(), nums.end());

        vector<vector<int>> dp(nums.size());
        for (int i = 0; i < nums.size(); i++) dp[i].push_back(nums[i]);

        vector<int> res = {};
        for (int i = nums.size() - 1; i >= 0; i--) {
            for (int j = i + 1; j < nums.size(); j++) {
                if (nums[j] % nums[i] == 0 && dp[j].size() + 1 > dp[i].size()) {
                    dp[i] = dp[j];
                    dp[i].push_back(nums[i]);
                }
            }
            res = dp[i].size() > res.size() ? dp[i] : res;
        }

        return res;
    }
};

void printRes(vector<int> res) {
    for (int i : res) {
        cout << i << " ";
    }
    cout << endl;
}

int main() {
    Solution sol;

    vector<int> input = { 1,2,3 };
    // vector<int> res = sol.largestDivisibleSubset(input);
    printRes(sol.largestDivisibleSubset(input));

    input = { 1,2,4,8 };
    printRes(sol.largestDivisibleSubset(input));

    return 0;
}