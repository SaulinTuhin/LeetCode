#include <iostream>
#include <string>
#include <vector>

using namespace std;

// Problem - 1347: https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/
// C++ Solution!
class Solution {
public:
    int minSteps(string s, string t) {
        vector<int> charCount(26, 0);

        for (int i = 0; i < s.size(); i++) {
            charCount[s[i] - 'a']++;
            charCount[t[i] - 'a']--;
        }

        int res = 0;
        for (int i = 0; i < 26; i++) {
            res += charCount[i] > 0 ? charCount[i] : 0;
        }

        return res;
    }
};

int main() {
    Solution sol;

    cout << sol.minSteps("bab", "aba") << endl;
    cout << sol.minSteps("leetcode", "practice") << endl;
    cout << sol.minSteps("anagram", "mangaar") << endl;

    return 0;
}