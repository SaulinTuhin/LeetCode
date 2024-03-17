#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Problem - 57: https://leetcode.com/problems/insert-interval/
// C++ Solution!
class Solution {
public:
	//	Find position of new Interval using linear search O(n)
	vector<vector<int>> insert_liner_traverse(vector<vector<int>>& intervals, vector<int>& newInterval) {
		vector<vector<int>> res;

		for (int i = 0; i < intervals.size(); i++) {
			if (newInterval[1] < intervals[i][0]) {
				res.push_back(newInterval);
				res.reserve(res.size() + intervals.size() - i);
				res.insert(res.end(), intervals.begin() + i, intervals.end());

				return res;
			}
			else if (newInterval[0] > intervals[i][1])
				res.push_back(intervals[i]);
			else
				newInterval = { min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1]) };
		}
		res.push_back(newInterval);

		return res;
	}

	//	Find position of new Interval using binary search O(logn)
	vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
		vector<vector<int>> res;

		auto start = lower_bound(intervals.begin(), intervals.end(), vector<int>({ newInterval[0], newInterval[0] }));
		if (start != intervals.begin() && newInterval[0] <= (*(start - 1))[1]) {
			start--;
			newInterval[0] = (*start)[0];
		}

		auto end = upper_bound(start, intervals.end(), vector<int>({ newInterval[1], newInterval[1] }));
		if (end != intervals.end() && newInterval[1] == (*end)[0]) {
			newInterval[1] = max(newInterval[1], (*end)[1]);
			end++;
		}
		else if (end != intervals.begin()) {
			newInterval[1] = max(newInterval[1], (*(end - 1))[1]);
		}

		res.reserve(intervals.size() - (end  - start) + 1);
		res.insert(res.end(), intervals.begin(), start);
		res.push_back(newInterval);
		res.insert(res.end(), end, intervals.end());

		return res;
	}
};

void printRes(vector<vector<int>> res) {
	for (auto row : res) {
		cout << "[";
		for (int col : row) {
			cout << col << ",";
		}
		cout << "],";
	}
	cout << endl;
}

int main() {
	Solution sol;

	vector<vector<int>> intervals = { {1,3}, {6,9} };
	vector<int> newInterval = { 2,5 };
	printRes(sol.insert(intervals, newInterval));

	intervals = { {1,2}, {3,5}, {6,7}, {8,10}, {12,16} };
	newInterval = { 4, 8 };
	printRes(sol.insert(intervals, newInterval));

	intervals = { {1,5} };
	newInterval = { 2, 3 };
	printRes(sol.insert(intervals, newInterval));

	intervals = { {2,4}, {5,7}, {8,10}, {11,13} };
	newInterval = { 3, 6 };
	printRes(sol.insert(intervals, newInterval));

	return 0;
}