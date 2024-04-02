#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

// Problem - 205: Isomorphic Strings
// C++ Solution!
class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_map<char, char> mST, mTS;
        for (int i = 0; i < s.size(); i++) {
            char c1 = s[i], c2 = t[i];
            if ((mST.find(c1) != mST.end() && mST[c1] != c2)
            || (mTS.find(c2) != mTS.end() && mTS[c2] != c1))
                return false;

            mST[c1] = c2;
            mTS[c2] = c1;
        }

        return true;
    }
};

int main() {
    Solution sol;

    cout << sol.isIsomorphic("egg", "add") << endl;

    cout << sol.isIsomorphic("foo", "bar") << endl;

    cout << sol.isIsomorphic("paper", "title") << endl;

    return 0;
}