#include <iostream>
#include <string>
#include <vector>

using namespace std;

// Problem - 791: https://leetcode.com/problems/custom-sort-string/
// C++ Solution!
class Solution {
public:
	string customSortString(string order, string s) {
		vector<int> freqMap(26, 0);
		string res = "";

		for (char i : s) {
			freqMap[i - 'a']++;
		}

		for (char i : order) {
			while (freqMap[i - 'a'] > 0) {
				res.push_back(i);
				freqMap[i - 'a']--;
			}
		}

		for (int i = 0; i < 26; i++) {
			while (freqMap[i] > 0) {
				res.push_back(i + 'a');
				freqMap[i]--;
			}
		}

		return res;
	}
};

int main() {
	Solution sol;

	cout << sol.customSortString("cba", "abcd") << endl;
	cout << sol.customSortString("bcafg", "abcd") << endl;

	return 0;
}