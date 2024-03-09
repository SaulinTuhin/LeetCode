#include <iostream>
#include <vector>

using namespace std;

// Problem - 2540: https://leetcode.com/problems/minimum-common-value/
// C++ Solution!
class Solution {
public:
	int getCommon(vector<int>& nums1, vector<int>& nums2) {
		int res = -1;
		int i = 0, j = 0;

		while (i < nums1.size() && j < nums2.size()) {
			if (nums1[i] == nums2[j]) {
				res = nums1[i];
				break;
			}
			else if (nums1[i] < nums2[j])
				i++;
			else
				j++;
		}

		return res;
	}
};

int main() {
	Solution sol;

	vector<int> input1 = { 1, 2, 3 };
	vector<int> input2 = { 2, 4 };
	cout << sol.getCommon(input1, input2) << endl;

	input1 = { 1, 2, 3, 6 };
	input2 = { 2, 3, 4, 5 };
	cout << sol.getCommon(input1, input2) << endl;

	return 0;
}