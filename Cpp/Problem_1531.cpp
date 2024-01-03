#include <iostream>
#include <string>
#include <algorithm>
#include <unordered_map>

using namespace std;

// Problem - 1531: https://leetcode.com/problems/string-compression-ii/
// C++ Solution!
class Solution {
public:
	struct Node {
		int i;
		int k;
		char prev_char;
		int prev_count;

		Node(int i, int k, char prev_char, int prev_count) {
			this->i = i;
			this->k = k;
			this->prev_char = prev_char;
			this->prev_count = prev_count;
		}

		bool operator==(const Node &n) const {
			return i == n.i && k == n.k && prev_char == n.prev_char && prev_count == n.prev_count;
		}
	};

	struct hash {
		size_t operator() (const Node &node) const {
			return node.i ^ node.k ^ node.prev_char ^ node.prev_count;
		}
	};

	int recursive_count(string& s, int i, int k, char prev_char, int prev_count, unordered_map <Node, int, hash> &cache) {
		if (cache.find({ i, k, prev_char, prev_count }) != cache.end())
			return cache[{i, k, prev_char, prev_count}];
		if (k < 0)
			return INT_MAX;
		if (i == s.length())
			return 0;

		int res = 0;
		if (s[i] == prev_char) {
			if (prev_count == 1 || prev_count == 9 || prev_count == 99) {
				res = 1 + recursive_count(s, i + 1, k, prev_char, prev_count + 1, cache);
			}
			else {
				res = recursive_count(s, i + 1, k, prev_char, prev_count + 1, cache);
			}
		}
		else {
			res = min(
				recursive_count(s, i + 1, k - 1, prev_char, prev_count, cache),
				1 + recursive_count(s, i + 1, k, s[i], 1, cache)
			);
		}

		cache[{i, k, prev_char, prev_count}] = res;
		return res;
	}

	int getLengthOfOptimalCompression(string s, int k) {
		unordered_map <Node, int, hash> cache;

		return recursive_count(s, 0, k, NULL, 0, cache);
	}
};

int main() {
	Solution sol;

	cout << sol.getLengthOfOptimalCompression("aaabcccd", 2) << endl;
	cout << sol.getLengthOfOptimalCompression("aabbaa", 2) << endl;
	cout << sol.getLengthOfOptimalCompression("aaaaaaaaaaa", 0) << endl;
	cout << sol.getLengthOfOptimalCompression("aabaabbcbbbaccc", 6) << endl;

	return 0;
}