#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

// Problem - 1624: https://leetcode.com/problems/largest-substring-between-two-equal-characters/
// C++ Solution!
class Solution {
public:
	int maxLengthBetweenEqualCharacters(string s) {
		vector<int> first_index(26, -1);

		int max_length = -1;
		for (int i = 0; i < s.size(); i++) {
			if (first_index[s[i] - 'a'] != -1) {
				max_length = max(max_length, i - first_index[s[i] - 'a'] - 1);
			}
			else {
				first_index[s[i] - 'a'] = i;
			}
		}

		return max_length;
	}
};

int main() {
	Solution sol;

	cout << sol.maxLengthBetweenEqualCharacters("aa") << endl;
	cout << sol.maxLengthBetweenEqualCharacters("abca") << endl;
	cout << sol.maxLengthBetweenEqualCharacters("cbzxy") << endl;

	return 0;
}