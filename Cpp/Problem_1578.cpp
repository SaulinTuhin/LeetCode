#include <iostream>
#include <string>
#include <vector>

using namespace std;

// Problem - 1578: https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
// C++ Solution!
class Solution {
public:
	int minCost(string colors, vector<int>& neededTime) {
		int first_baloon = 0, result = 0;

		for (int second_baloon = 1; second_baloon < colors.size(); second_baloon++) {
			if (colors[first_baloon] == colors[second_baloon]) {
				if (neededTime[first_baloon] < neededTime[second_baloon]) {
					result += neededTime[first_baloon];

					first_baloon = second_baloon;
				}
				else {
					result += neededTime[second_baloon];
				}
			}
			else {
				first_baloon = second_baloon;
			}
		}

		return result;
	}
};

int main() {
	Solution sol;

	vector <int> input = { 1, 2, 3, 4, 5 };
	cout << sol.minCost("abaac", input) << endl;

	input = { 1, 2, 3 };
	cout << sol.minCost("abc", input) << endl;

	input = { 1, 2, 3, 4, 1 };
	cout << sol.minCost("aabaa", input) << endl;

	return 0;
}