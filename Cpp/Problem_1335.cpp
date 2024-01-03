#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

// Problem - 1335: https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/
// C++ Solution!
const int max_i = 300;
const int max_d = 10;
const int max_cur_max = 1000;
const int max_difficulty = 10000;

class Solution {
public:
	struct Node {
		int i, d, cur_max;

		Node(int i, int d, int cur_max) {
			this->i = i;
			this->d = d;
			this->cur_max = cur_max;
		}

		bool operator ==(const Node &n) const {
			return i == n.i && d == n.d && cur_max == n.cur_max;
		}
	};

	struct hash {
		size_t operator()(const Node &node) const {
			int key = abs(node.cur_max);
			key = key * max_d + node.d;
			key = key * max_i + node.i;

			return key;
		}
	};

	int find_difficulty(int i, int d, int cur_max, vector<int>& jobDifficulty, unordered_map<Node, int, hash>& cache) {
		if (i == jobDifficulty.size())
			return d == 0 ? 0 : max_difficulty;
		if (d == 0)
			return max_difficulty;
		if (cache.find({ i, d, cur_max }) != cache.end())
			return cache[{i, d, cur_max}];

		cur_max = max(cur_max, jobDifficulty[i]);
		int res = min(
			find_difficulty(i + 1, d, cur_max, jobDifficulty, cache),
			cur_max + find_difficulty(i+1, d - 1, -1, jobDifficulty, cache)
		);

		cache[{i, d, cur_max}] = res;
		return res;
	}

	int minDifficulty(vector<int>& jobDifficulty, int d) {
		if (jobDifficulty.size() < d)
			return -1;

		unordered_map <Node, int, hash> cache;

		return find_difficulty(0, d, -1, jobDifficulty, cache);
	}
};

int main() {
	Solution sol;

	vector<int> input = { 6, 5, 4, 3, 2, 1 };
	cout << sol.minDifficulty(input, 2) << endl;

	input = { 9, 9, 9 };
	cout << sol.minDifficulty(input, 4) << endl;

	input = { 1, 1, 1 };
	cout << sol.minDifficulty(input, 3) << endl;

	return 0;
}