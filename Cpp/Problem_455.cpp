#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Problem - 455: https://leetcode.com/problems/assign-cookies/
// C++ Solution!
class Solution {
public:
	int findContentChildren(vector<int>& g, vector<int>& s) {
		sort(g.begin(), g.end());
		sort(s.begin(), s.end());

		int i = 0, j = 0;
		while (i < g.size()) {
			while (j < s.size() && g[i] > s[j]) {
				j++;
			}
			if (j == s.size())
				break;

			i++;
			j++;
		}

		return i;
	}
};

int main() {
	Solution sol;

	vector <int> g = { 1, 2, 3 }, s = { 1,1 };
	cout << sol.findContentChildren(g, s) << endl;
	g = { 1, 2 }, s = { 1, 2, 3 };
	cout << sol.findContentChildren(g, s) << endl;

	return 0;
}