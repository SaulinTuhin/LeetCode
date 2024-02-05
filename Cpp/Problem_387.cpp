#include <iostream>
#include <string>
#include <vector>

using namespace std;

// Problem - 387: https://leetcode.com/problems/first-unique-character-in-a-string/
// C++ Solution!
class Solution {
public:
    int firstUniqChar(string s) {
        vector<int> freq(26, 0);

        for (char i : s) freq[i - 'a']++;
        for (int i = 0; i < s.size(); i++) if (freq[s[i] - 'a'] == 1) return i;

        return -1;
    }
};

int main() {
    Solution sol;

    cout << sol.firstUniqChar("leetcode") << endl;
    cout << sol.firstUniqChar("loveleetcode") << endl;
    cout << sol.firstUniqChar("aabb") << endl;

    return 0;
}