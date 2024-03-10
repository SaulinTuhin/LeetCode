#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

// Problem - 349: https://leetcode.com/problems/intersection-of-two-arrays/
// C++ Solution!
class Solution {
public:
	vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
		unordered_set<int> us(nums1.begin(), nums1.end());
		vector<int> res;

		for (int i : nums2) {
			if (us.find(i) != us.end()) {
				res.push_back(i);
				us.erase(i);
			}
		}

		return res;
	}
};

void printRes(vector<int> res) {
	for (int i : res)
		cout << i << " ";

	cout << endl << endl;
}

int main() {
	Solution sol;

	vector<int> input1 = { 1,2,2,1 }, input2 = { 2, 2 };
	printRes(sol.intersection(input1, input2));

	input1 = { 4, 9, 5 }, input2 = { 9, 4, 9, 8, 4 };
	printRes(sol.intersection(input1, input2));

	return 0;
}