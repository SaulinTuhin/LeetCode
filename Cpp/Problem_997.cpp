#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

// Problem - 997: https://leetcode.com/problems/find-the-town-judge/
// C++ Solution!
class Solution {
public:
	int findJudge(int n, vector<vector<int>>& trust) {
		unordered_map<int, int> delta;

		for (auto i : trust) {
			delta[i[0]]--;
			delta[i[1]]++;
		}

		for (int i = 1; i <= n; i++)
			if (delta[i] == n - 1) return i;

		return -1;
	}
};

int main() {
	Solution sol;

	vector<vector<int>> input = { {1, 2} };
	cout << sol.findJudge(2, input) << endl;

	input = { {1, 3}, {2, 3} };
	cout << sol.findJudge(3, input) << endl;

	input = { {1, 3}, {2, 3}, {3, 1} };
	cout << sol.findJudge(3, input) << endl;

	return 0;
}