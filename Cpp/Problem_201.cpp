#include <iostream>

using namespace std;

// Problem - 201: https://leetcode.com/problems/bitwise-and-of-numbers-range/
// C++ Solution!
class Solution {
public:
	int rangeBitwiseAnd(int left, int right) {
		int i;
		for (i = 0; left != right; i++) {
			left >>= 1;
			right >>= 1;
		}

		return left << i;
	}
};

int main() {
	Solution sol;

	cout << sol.rangeBitwiseAnd(5, 7) << endl;
	cout << sol.rangeBitwiseAnd(0, 0) << endl;
	cout << sol.rangeBitwiseAnd(1, 2147483647) << endl;

	return 0;
}