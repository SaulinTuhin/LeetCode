#include <iostream>
#include <string>

using namespace std;

// Problem - 1614: Maximum Nesting Depth of the Parentheses
// C++ Solution!
class Solution {
public:
    int maxDepth(string s) {
        int res = 0;
        int curDepth = 0;

        for (char i : s) {
            if (i == '(')
                curDepth++;
            else if (i == ')')
                curDepth--;

            res = max(res, curDepth);
        }

        return res;
    }
};

int main() {
    Solution sol;

    cout << sol.maxDepth("(1+(2*3)+((8)/4))+1") << endl;
    cout << sol.maxDepth("(1)+((2))+(((3)))") << endl;

    return 0;
}