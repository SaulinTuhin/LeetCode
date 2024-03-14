#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

// Problem - 930: https://leetcode.com/problems/binary-subarrays-with-sum/
// C++ Solution!
class Solution {
public:
	//	Prefix Sum: O(n)->Runtime | O(n)->Memory
	int numSubarraysWithSum_prefixSum(vector<int>& nums, int goal) {
		int result = 0;
		unordered_map<int, int> mp;
		mp[0] = 1;

		int prefixSum = 0;
		for (int i : nums) {
			prefixSum += i;
			result += mp[prefixSum - goal];
			mp[prefixSum]++;
		}

		return result;
	}

	//	Modified Sliding Window: O(n)->Runtime | O(1)->Memory
	int helper(vector<int>& nums, int goal) {
		if (goal < 0)
			return 0;

		int res = 0, l = 0, curSum = 0;
		for (int r = 0; r < nums.size(); r++) {
			curSum += nums[r];

			while (curSum > goal) {
				curSum -= nums[l];
				l++;
			}
			res += (r - l) + 1;
		}

		return res;
	}
	int numSubarraysWithSum(vector<int>& nums, int goal) {
		return helper(nums, goal) - helper(nums, goal - 1);
	}
};

int main() {
	Solution sol;

	vector<int> input = { 1, 0, 1, 0, 1 };
	cout << sol.numSubarraysWithSum_prefixSum(input, 2) << endl;
	cout << sol.numSubarraysWithSum(input, 2) << endl;

	input = { 0, 0, 0, 0, 0 };
	cout << sol.numSubarraysWithSum_prefixSum(input, 0) << endl;
	cout << sol.numSubarraysWithSum(input, 0) << endl;

	return 0;
}