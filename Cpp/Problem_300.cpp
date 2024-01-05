#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Problem - 300: https://leetcode.com/problems/longest-increasing-subsequence/
// C++ Solution!
class Solution {
public:
	//	DP solution
	//	O(n^2)
	/*int lengthOfLIS(vector<int>& nums) {
		int n = nums.size(), res = 1;
		vector<int> dp(n, 1);

		for (int i = n - 1; i >= 0; i--) {
			for (int j = i + 1; j < n; j++) {
				if (nums[j] > nums[i]) {
					dp[i] = max(dp[i], 1 + dp[j]);

					if (dp[i] > res)
						res = dp[i];
				}
			}
		}

		return res;
	}*/

	//	Incomplete Patience Sorting
	//	O(nLogn)
	int lengthOfLIS(vector<int>& nums) {
		int n = nums.size(), res = 1;
		vector<int> pile;
		pile.push_back(nums[0]);

		for (int i = 1; i < n; i++) {
			if (nums[i] > pile.back()) {
				pile.push_back(nums[i]);
				res++;
			}
			else {
				auto it = lower_bound(pile.begin(), pile.end(), nums[i]);
				*it = nums[i];
			}
		}

		return res;
	}
};

int main() {
	Solution sol;

	vector<int> input = { 10, 9, 2, 5, 3, 7, 101, 18 };
	cout << sol.lengthOfLIS(input) << endl;
	input = { 0, 1, 0, 3, 2, 3 };
	cout << sol.lengthOfLIS(input) << endl;
	input = { 7, 7, 7, 7, 7, 7, 7 };
	cout << sol.lengthOfLIS(input) << endl;

	return 0;
}