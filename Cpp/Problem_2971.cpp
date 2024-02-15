#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Problem - 2971: https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/
// C++ Solution!
class Solution {
public:
	long long largestPerimeter_forward(vector<int>& nums) {	// O(nlogn)
		sort(nums.begin(), nums.end());	// O(nlogn)

		long long res = -1;
		long long prevTotal = 0;
		for (int cur : nums) {	// O(n)
			if (prevTotal > cur)
				res = prevTotal + cur;
			prevTotal += cur;
		}

		return res;
	}

	//	Forward traverse. If calculating the sum during sort was
	//	possible, it would've been better than forward traverse.
	long long largestPerimeter(vector<int>& nums) {	// O(nlogn)
		sort(nums.begin(), nums.end());	// O(nlogn)

		long long sum = 0;
		for (int i : nums) sum += i;	// O(n)

		for (int i = nums.size() - 1; i >= 2; i--) {	// O(n)
			sum -= nums[i];

			if (sum > nums[i])
				return sum + nums[i];
		}

		return -1;
	}
};

int main() {
	Solution sol;

	vector<int> input = { 5, 5, 5 };
	cout << sol.largestPerimeter(input) << endl;

	input = { 1, 12, 1, 2, 5, 50, 3 };
	cout << sol.largestPerimeter(input) << endl;

	input = { 5, 5, 50 };
	cout << sol.largestPerimeter(input) << endl;

	return 0;
}