#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
	bool isAnagram(string s, string t) {
		if (s.size() != t.size()) {
			return false;
		}

		vector <int> hash(26, 0);
		int result = 0;
		for (int i = 0; i < s.size(); i++) {
			++hash[s[i] - 'a'] <= 0 ? --result : ++result;
			--hash[t[i] - 'a'] >= 0 ? --result : ++result;
		}

		return !result;
	}
};

int main() {

	Solution sol;

	string s1 = "anagram", t1 = "nagaram";
	string s2 = "rat", t2 = "car";
	string s3 = "aa", t3 = "bb";

	cout << sol.isAnagram(s1, t1) << endl;
	cout << sol.isAnagram(s2, t2) << endl;
	cout << sol.isAnagram(s3, t3) << endl;

	return 0;
}