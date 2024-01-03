#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
	int minOperations(string s) {
		int operations = 0;

		for (int i = 0; i < s.size(); i++) {
			if (i % 2 == 0)
				s[i] != '0' ? operations++ : true;
			else
				s[i] != '1' ? operations++ : true;
		}

		return min(operations, int(s.size()) - operations);
	}
};

int main() {
	Solution sol;

	cout << sol.minOperations("0100") << endl;
	cout << sol.minOperations("10") << endl;
	cout << sol.minOperations("1111") << endl;

	return 0;
}