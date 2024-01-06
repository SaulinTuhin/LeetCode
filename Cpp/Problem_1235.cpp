#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Problem - 1235: https://leetcode.com/problems/maximum-profit-in-job-scheduling/
// C++ Solution!
class Solution {
public:
	int find(int i, vector<vector<int>>& jobs, vector<int>& startTime, vector<int>& dp) {
		int n = jobs.size();
		if (i >= n)
			return 0;
		if (dp[i] != -1)
			return dp[i];

		//	don't include current job
		int notInclude = find(i + 1, jobs, startTime, dp);

		//	include current job
		int index = lower_bound(startTime.begin() + i + 1, startTime.end(), jobs[i][1]) - startTime.begin();
		int include = jobs[i][2] + find(index, jobs, startTime, dp);

		return dp[i] = max(notInclude, include);
	}

	int jobScheduling(vector<int>& startTime, vector<int>& endTime, vector<int>& profit) {
		int n = profit.size();
		vector<vector<int>> jobs;
		vector<int> dp(n, -1);

		for (int i = 0; i < n; i++) {
			jobs.push_back({ startTime[i], endTime[i], profit[i] });
		}

		sort(jobs.begin(), jobs.end());
		sort(startTime.begin(), startTime.end());

		return find(0, jobs, startTime, dp);
	}

	/*int jobScheduling(vector<int>& startTime, vector<int>& endTime, vector<int>& profit) {
		int n = startTime.size();
		vector<pair<int, int>> st(n);
		for (int i = 0; i < n; i++) 
			st[i] = { startTime[i], i };
		sort(st.begin(), st.end());
		vector<int> dp(n + 1, 0);
		for (int i = n - 1; i > -1; i--)
			dp[i] += max(dp[i + 1], profit[st[i].second] + dp[lower_bound(st.begin() + i, st.end(), make_pair(endTime[st[i].second], 0)) - st.begin()]);
		return dp[0];
	}*/
};

int main() {
	Solution sol;

	vector<int> startTime = { 1, 2, 3, 3 }, endTime = { 3, 4, 5, 6 }, profit = { 50, 10, 40, 70 };
	cout << sol.jobScheduling(startTime, endTime, profit) << endl;
	startTime = { 1, 2, 3, 4, 6 }, endTime = { 3, 5, 10, 6, 9 }, profit = { 20, 20, 100, 70, 60 };
	cout << sol.jobScheduling(startTime, endTime, profit) << endl;
	startTime = { 1, 1, 1 }, endTime = { 2, 3, 4 }, profit = { 5, 6, 4 };
	cout << sol.jobScheduling(startTime, endTime, profit) << endl;

	return 0;
}