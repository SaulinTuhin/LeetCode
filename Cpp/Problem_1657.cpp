#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

// Problem - 1657: https://leetcode.com/problems/determine-if-two-strings-are-close/
// C++ Solution!
class Solution {
public:
    bool closeStrings(string word1, string word2) {
        if (word1.length() != word2.length())
            return false;

        vector<int> freq1(26, 0);
        vector<int> freq2(26, 0);
        for (int i = 0; i < word1.length(); i++) {
            freq1[word1[i] - 'a']++;
            freq2[word2[i] - 'a']++;
        }

        for (int i = 0; i < 26; i++) {
            if (freq1[i] == 0 != freq2[i] == 0)
                return false;
        }

        sort(freq1.begin(), freq1.end());
        sort(freq2.begin(), freq2.end());

        for (int i = 0; i < 26; i++) {
            if (freq1[i] != freq2[i])
                return false;
        }
        return true;
    }
};

int main() {
    Solution sol;

    cout << sol.closeStrings("abc", "bca") << endl;
    cout << sol.closeStrings("a", "aa") << endl;
    cout << sol.closeStrings("cabbba", "abbccc") << endl;

    return 0;
}