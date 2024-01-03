#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

// Problem - 2610: https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/
// C++ Solution!
class Solution {
public:
	vector<vector<int>> findMatrix(vector<int>& nums) {
		unordered_map <int, int> numCount;

		vector<vector<int>> res;
		for (int num : nums) {
			int row = numCount[num];

			if (row == res.size()) {
				res.push_back({ });
			}
			res[row].push_back(num);
			numCount[num]++;
		}

		return res;
	}
};

void printVector(vector<vector<int>> res) {
	for (vector<int> row : res) {
		for (int val : row) {
			cout << val << " ";
		}
		cout << endl;
	}
	cout << endl;
}

int main() {
	Solution sol;

	vector <int> input = { 1, 3, 4, 1, 2, 3, 1 };
	printVector(sol.findMatrix(input));
	input = { 2, 1, 1 };
	printVector(sol.findMatrix(input));

	return 0;
}