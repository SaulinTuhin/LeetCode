#include <iostream>

using namespace std;

// Problem - 231: https://leetcode.com/problems/power-of-two/
// C++ Solution!
class Solution {
public:
	//	Loop
	bool isPowerOfTwo_loop(int n) {
		long i = 1;
		while (i < n)
			i *= 2;

		return i == n;
	}

	//	Bit manipulation
	bool isPowerOfTwo_bitManipulation(int n) {
		return n > 0 && (n & (n - 1)) == 0;
	}

	//	Math
	bool isPowerOfTwo(int n) {
		return n > 0 && ((1 << 30) % n) == 0;
	}
};

int main() {
	Solution sol;

	cout << sol.isPowerOfTwo(1) << endl;
	cout << sol.isPowerOfTwo(16) << endl;
	cout << sol.isPowerOfTwo(3) << endl;

	return 0;
}