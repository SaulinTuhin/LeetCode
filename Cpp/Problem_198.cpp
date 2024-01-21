#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Problem - 198: https://leetcode.com/problems/house-robber/
// C++ Solution!
class Solution {
public:
	int rob(vector<int>& nums) {
		int prev2_max = 0, prev_max = 0;

		for (int cur : nums) {
			int temp = max(cur + prev2_max, prev_max);
			prev2_max = prev_max;
			prev_max = temp;
		}

		return prev_max;
	}
};

int main() {
	Solution sol;

	vector<int> input = { 1, 2, 3, 1 };
	cout << sol.rob(input) << endl;
	input = { 2, 7, 9, 3, 1 };
	cout << sol.rob(input) << endl;

	return 0;
}