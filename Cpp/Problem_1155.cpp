#include <iostream>
#include <unordered_map>

using namespace std;

/*
Problem - 1155: https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
C++ Solution!
*/
class Solution {
public:
	const int mod = pow(10, 9) + 7;

	struct pair_hash {
		size_t operator()(const pair<int, int> &v) const {
			return v.first * 31 + v.second;
		}
	};

	int recursive_rolls(int n, const int k, int target, unordered_map <pair<int, int>, int, pair_hash> &cache) {
		if (n == 0)
			return target == 0 ? 1 : 0;
		if (target < 0)
			return 0;

		if (cache.find({ n, target }) != cache.end()) {
			return cache[{n, target}];
		}

		int res = 0;
		for (int cur_roll = 1; cur_roll <= k; cur_roll++) {
			res = (res + recursive_rolls(n - 1, k, target - cur_roll, cache)) % mod;
		}
		cache[{n, target}] = res;
		return res;
	}

	int numRollsToTarget(int n, int k, int target) {
		//	Recursive solution
		//unordered_map <pair<int, int>, int, pair_hash> cache;
		//return recursive_rolls(n, k, target, cache);

		//	Dynamic Programming solution
		vector <int> dp(target + 1, 0);
		dp[0] = 1;

		for (int dice = 0; dice < n; dice++) {
			vector <int> next_dp(target + 1, 0);

			for (int cur_roll = 1; cur_roll <= k; cur_roll++) {
				for (int cur_total = cur_roll; cur_total <= target; cur_total++) {
					next_dp[cur_total] = (next_dp[cur_total] + dp[cur_total - cur_roll]) % mod;
				}
			}
			dp = next_dp;
		}

		return dp[target];
	}
};

int main() {
	Solution sol;

	cout << sol.numRollsToTarget(1, 6, 3) << endl;
	cout << sol.numRollsToTarget(2, 6, 7) << endl;
	cout << sol.numRollsToTarget(30, 30, 500) << endl;
	
	return 0;
}