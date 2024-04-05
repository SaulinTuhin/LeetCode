#include <iostream>
#include <string>
#include <stack>

using namespace std;

// Problem - 1544: Make The String Great
// C++ Solution!
class Solution {
public:
    string makeGood(string s) {
        stack<char> st;
        string res = "";
        for (char i : s) {
            if (!st.empty() && abs(st.top() - i) == ('a' - 'A'))
                st.pop();
            else
                st.push(i);
        }

        while (!st.empty()) {
            res = st.top() + res;
            st.pop();
        }

        return res;
    }
};

int main() {
    Solution sol;

    cout << sol.makeGood("leEeetcode") << endl;
    cout << sol.makeGood("abBAcC") << endl;
    cout << sol.makeGood("s") << endl;

    return 0;
}