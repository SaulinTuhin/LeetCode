#include <iostream>
#include <cmath>

using namespace std;

// Problem - 2485: https://leetcode.com/problems/find-the-pivot-integer/
// C++ Solution!
class Solution {
public:
    int pivotInteger(int n) {
        double pivot = sqrt(n * (n + 1) / 2);

        return pivot - ceil(pivot) == 0 ? int(pivot) : -1;
    }
};

int main() {
    Solution sol;

    cout << sol.pivotInteger(8) << endl;
    cout << sol.pivotInteger(1) << endl;
    cout << sol.pivotInteger(4) << endl;

    return 0;
}