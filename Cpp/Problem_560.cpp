#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

// Problem - 560: https://leetcode.com/problems/subarray-sum-equals-k/
// C++ Solution!
class Solution {
public:
	int subarraySum(vector<int>& nums, int k) {
		int res = 0, curSum = 0;
		unordered_map<int, int> prefixSums;
		prefixSums[0] = 1;

		for (int i : nums) {
			curSum += i;

			res += prefixSums[curSum - k];
			prefixSums[curSum]++;
		}

		return res;
	}
};

int main() {
	Solution sol;

	vector<int> input = { 1,1,1 };
	cout << sol.subarraySum(input, 2) << endl;
	
	input = { 1, 2, 3 };
	cout << sol.subarraySum(input, 3) << endl;

	return 0;
}