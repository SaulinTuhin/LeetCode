#include <iostream>
#include <vector>
#include <unordered_map>
#include <cmath>

using namespace std;

// Problem - 2870: https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/
// C++ Solution!
class Solution
{
public:
	int minOperations(vector<int> &nums)
	{
		unordered_map<int, int> counts;

		for (int num : nums)
		{
			counts[num]++;
		}

		int res = 0;
		for (auto count : counts)
		{
			if (count.second == 1)
				return -1;

			res += ceil((double)count.second / 3);
		}

		return res;
	}
};

int main()
{
	Solution sol;

	vector<int> input = { 2, 3, 3, 2, 2, 4, 2, 3, 4 };
	cout << sol.minOperations(input) << endl;
	input = { 2, 1, 2, 2, 3, 3 };
	cout << sol.minOperations(input) << endl;

	return 0;
}