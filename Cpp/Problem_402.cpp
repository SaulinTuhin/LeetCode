#include <iostream>
#include <string>

using namespace std;

// Problem - 402: https://leetcode.com/problems/remove-k-digits/
// C++ Solution!
class Solution {
public:
    string removeKdigits(string num, int k) {
        string ans = "";
        for (char c : num) {
            while (k > 0 && !ans.empty() && ans.back() > c) {
                k--;
                ans.erase(ans.end() - 1);
            }
            ans += c;
        }

        ans = ans.substr(0, ans.size() - k);
        size_t p = ans.find_first_not_of('0');
        return p == string::npos ? "0" : ans.substr(p);
    }
};

int main() {
    Solution sol;

    cout << sol.removeKdigits("1432219", 3) << endl;
    cout << sol.removeKdigits("10200", 1) << endl;
    cout << sol.removeKdigits("10", 2) << endl;
    cout << sol.removeKdigits("9", 1) << endl;
    cout << sol.removeKdigits("112", 1) << endl;

    return 0;
}