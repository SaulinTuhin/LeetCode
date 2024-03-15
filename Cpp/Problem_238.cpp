#include <iostream>
#include <vector>

using namespace std;

// Problem - 238: https://leetcode.com/problems/product-of-array-except-self/
// C++ Solution!
class Solution {
public:
	vector<int> productExceptSelf(vector<int>& nums) {
		vector<int> res(nums.size(), 1);

		for (int i = 0; i < nums.size() - 1; i++) {
			res[i + 1] = res[i] * nums[i];
		}

		int postfix = 1;
		for (int i = nums.size() - 1; i > 0; i--) {
			postfix *= nums[i];
			res[i - 1] *= postfix;
		}

		return res;
	}
};

void printRes(vector<int> res) {
	for (int i : res)
		cout << i << ",";
	cout << endl;
}

int main() {
	Solution sol;

	vector<int> input = { 1,2,3,4 };
	printRes(sol.productExceptSelf(input));

	input = { -1,1,0,-3,3 };
	printRes(sol.productExceptSelf(input));

	return 0;
}