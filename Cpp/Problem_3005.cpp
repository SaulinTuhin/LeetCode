#include <iostream>
#include <vector>

using namespace std;

// Problem - 3005: https://leetcode.com/problems/count-elements-with-maximum-frequency/
// C++ Solution!
class Solution {
public:
	int maxFrequencyElements(vector<int>& nums) {
		int max_freq = -1, res = 0;
		vector<int> freqMap(101, 0);

		for (int i : nums) {
			freqMap[i]++;

			if (freqMap[i] == max_freq)
				res += freqMap[i];
			else if (freqMap[i] > max_freq) {
				res = freqMap[i];
				max_freq = freqMap[i];
			}
		}

		return res;
	}
};

int main() {
	Solution sol;

	vector<int> input = { 1, 2, 2, 3, 1, 4 };
	cout << sol.maxFrequencyElements(input) << endl;

	input = { 1, 2, 3, 4, 5 };
	cout << sol.maxFrequencyElements(input) << endl;

	return 0;
}