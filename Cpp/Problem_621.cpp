#include <iostream>
#include <vector>
#include <queue>

using namespace std;

// Problem - 621: https://leetcode.com/problems/task-scheduler/
// C++ Solution!
class Solution {
public:
	int leastInterval(vector<char>& tasks, int n) {
		vector<int> freqMap(26, 0);
		for (char i : tasks) freqMap[i - 'A']++;
		sort(freqMap.begin(), freqMap.end());

		int batchCount = freqMap[25] - 1;
		int idleCyles = batchCount * n;

		for (int i = 0; i < 25; i++) {
			idleCyles -= min(freqMap[i], batchCount);
		}

		return idleCyles > 0 ? tasks.size() + idleCyles : tasks.size();
	}
};

int main() {
	Solution sol;

	vector<char> input = { 'A', 'A', 'A', 'B', 'B', 'B' };
	cout << sol.leastInterval(input, 2) << endl;

	input = { 'A', 'C', 'A', 'B', 'D', 'B' };
	cout << sol.leastInterval(input, 1) << endl;

	input = { 'A', 'A', 'A', 'B', 'B', 'B' };
	cout << sol.leastInterval(input, 3) << endl;

	return 0;
}