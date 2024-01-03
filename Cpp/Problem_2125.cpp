#include <iostream>
#include <vector>
#include <string>

using namespace std;

// Problem - 2125: https://leetcode.com/problems/number-of-laser-beams-in-a-bank/
// C++ Solution!
class Solution {
public:
	int numberOfBeams(vector<string>& bank) {
		int lastRowCount = 0, thisRowCount = 0, res = 0;

		for (string row : bank) {
			for (char ch : row) {
				if (ch == '1') {
					thisRowCount++;
				}
			}

			if (thisRowCount) {
				res += lastRowCount * thisRowCount;
				lastRowCount = thisRowCount;
				thisRowCount = 0;
			}
		}

		return res;
	}
};

int main() {
	Solution sol;

	vector<string> input = { "011001", "000000", "010100", "001000" };
	cout << sol.numberOfBeams(input) << endl;
	input = { "000", "111", "000" };
	cout << sol.numberOfBeams(input) << endl;

	return 0;
}