#include <iostream>
#include <vector>
#include <string>

using namespace std;

// Problem - 1897: https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/
// C++ Solution!
class Solution {
public:
	bool makeEqual(vector<string>& words) {
		vector<int> ch_frequency(26, 0);

		for (string word : words) {
			for (char ch : word) {
				ch_frequency[ch - 'a']++;
			}
		}

		for (int i = 0; i < 26; i++) {
			if (ch_frequency[i] % words.size() != 0)
				return false;
		}

		return true;
	}
};

int main() {
	Solution sol;

	vector<string> input = { "abc", "aabc", "bc" };
	cout << sol.makeEqual(input) << endl;
	input = { "ab", "a" };
	cout << sol.makeEqual(input) << endl;

	return 0;
}