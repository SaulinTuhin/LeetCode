#include <iostream>
#include <string>
#include <vector>

using namespace std;

// Problem - 91: https://leetcode.com/problems/decode-ways/
// C++
class Solution {
public:
	int recursive(string s, int i, vector<int> &mem) {
		if (i == s.size())
			return 1;
		
		if (s[i] == '0')
			return 0;

		if (mem[i] != -1)
			return mem[i];

		int count = recursive(s, i + 1, mem);

		if (i + 1 < s.size() && (s[i] == '1' || (s[i] == '2' && s[i + 1] <= '6'))) {
			count += recursive(s, i + 2, mem);
		}

		mem[i] = count;
		return count;
	}

	int numDecodings(string s) {
		// Recursive solution
		//vector<int> mem(s.size(), -1);
		//return recursive(s, 0, mem);

		int n = s.size();
		vector<int> dp(n + 1, 0);

		dp[n] = 1;
		for (int i = n - 1; i >= 0; i--) {
			if (s[i] != '0') dp[i] += dp[i + 1];

			if (i+1 < n && (s[i] == '1' || (s[i] == '2' && s[i + 1] <= '6')))
				dp[i] += dp[i + 2];
		}

		return dp[0];
	}
};

int main() {
	Solution sol;

	cout << sol.numDecodings("12") << endl;
	cout << sol.numDecodings("226") << endl;
	cout << sol.numDecodings("06") << endl;

	return 0;
}