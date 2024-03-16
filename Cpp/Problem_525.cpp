#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

// Problem - 525: https://leetcode.com/problems/contiguous-array/
// C++ Solution!
class Solution {
public:
	int findMaxLength(vector<int>& nums) {
		int res = 0, zero = 0, one = 0;
		unordered_map<int, int> mp;
		
		for (int i = 0; i < nums.size(); i++) {
			if (nums[i])
				one++;
			else
				zero++;

			if (mp.find(one - zero) == mp.end())
				mp[one - zero] = i;

			if (one == zero)
				res = one + zero;
			else {
				int min_prefix = mp[one - zero];
				if (i - min_prefix > res)
					res = i - min_prefix;
			}
		}

		return res;
	}
};

int main() {
	Solution sol;

	vector<int> input = { 0,1 };
	cout << sol.findMaxLength(input) << endl;

	input = { 0,1,0 };
	cout << sol.findMaxLength(input) << endl;

	input = { 0,0,0,1,1,1,0 };
	cout << sol.findMaxLength(input) << endl;

	input = { 0,0,1,0,0,0,1,1 };
	cout << sol.findMaxLength(input) << endl;

	return 0;
}