#include <iostream>
#include <string>
#include <unordered_set>

using namespace std;

/*
Problem - 1496: https://leetcode.com/problems/path-crossing/
C++ Solution!
*/
class Solution {
public:
	struct hashFunction {
		size_t operator()(const pair<int, int> &x) const {
			return x.first ^ x.second;
		}
	};

	struct pair_hash {
		size_t operator()(const pair<int, int> &v) const {
			return v.first * 31 + v.second;
		}
	};

	bool isPathCrossing(string path) {
		int x_pos = 0, y_pos = 0;
		unordered_set<pair<int, int>, pair_hash> prev_pos;
		prev_pos.insert({ 0, 0 });

		for (char i : path) {
			switch (i)
			{
			case 'N':
				x_pos++;
				break;
			case 'S':
				x_pos--;
				break;
			case 'E':
				y_pos++;
				break;
			case 'W':
				y_pos--;
				break;
			default:
				break;
			}

			if (prev_pos.find({ x_pos, y_pos }) != prev_pos.end())
				return true;
			else
				prev_pos.insert({ x_pos, y_pos });
		}

		return false;
	}
};

int main() {
	Solution sol;

	cout << sol.isPathCrossing("NES") << endl;
	cout << sol.isPathCrossing("NESWW") << endl;

	return 0;
}