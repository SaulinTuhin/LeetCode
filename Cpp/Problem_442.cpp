#include <iostream>
#include <vector>

using namespace std;

// Problem - 442: https://leetcode.com/problems/find-all-duplicates-in-an-array/
// C++ Solution!
class Solution {
public:
	vector<int> findDuplicates(vector<int>& nums) {
		vector<int> res;

		for (int i : nums) {
			i = abs(i);
			if (nums[i - 1] < 0)
				res.push_back(i);
			nums[i - 1] *= -1;
		}

		return res;
	}
};

void printRes(vector<int> res) {
	for (int i = 0; i < res.size(); i++) {
		cout << res[i] << ",";
	}
	cout << endl;
}

int main() {
	Solution sol;

	vector<int> input = { 4,3,2,7,8,2,3,1 };
	printRes(sol.findDuplicates(input));

	input = { 1,1,2 };
	printRes(sol.findDuplicates(input));

	input = { 1 };
	printRes(sol.findDuplicates(input));

	return 0;
}