#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

// Problem - 446: https://leetcode.com/problems/arithmetic-slices-ii-subsequence/
// C++ Solution!
class Solution {
public:
	int numberOfArithmeticSlices(vector<int>& nums) {
		int n = nums.size(), res = 0;
		vector<unordered_map<int, int>> dp(n);

		for (int i = n - 1; i > -1; i--) {
			for (int j = i + 1; j < n; j++) {
				long long long_diff = static_cast<long long>(nums[j]) - nums[i];
				if (long_diff > INT_MAX || long_diff < INT_MIN)
					continue;
				int diff = static_cast<int>(long_diff);

				dp[i][diff] += 1 + dp[j][diff];

				res += dp[j][diff];
			}
		}

		return res;
	}
};

int main() {
	Solution sol;

	vector<int> input = { 2, 4, 6, 8, 10 };
	cout << sol.numberOfArithmeticSlices(input) << endl;
	input = { 7, 7, 7, 7, 7 };
	cout << sol.numberOfArithmeticSlices(input) << endl;
	input = { 0, 2000000000, -294967296 };
	cout << sol.numberOfArithmeticSlices(input) << endl;

	return 0;
}