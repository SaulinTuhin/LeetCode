#include <iostream>
#include <vector>

using namespace std;

// Problem - 645: https://leetcode.com/problems/set-mismatch/
// C++ Solution!
class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        vector<int> res = { 0, 0 }; //  {duplicate, missing}

        for (int curNum : nums) {
            curNum = abs(curNum);
            nums[curNum - 1] = -1 * nums[curNum - 1];
            if (nums[curNum - 1] > 0)
                res[0] = curNum;
        }

        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] > 0 && i + 1 != res[0]) {
                res[1] = i + 1;
                return res;
            }
        }

        return res;
    }
};

int main() {
    Solution sol;

    vector<int> input = { 1,2,2,4 };
    vector<int> res = sol.findErrorNums(input);
    cout << res[0] << " " << res[1] << endl;
    input = { 1,1 };
    res = sol.findErrorNums(input);
    cout << res[0] << " " << res[1] << endl;
    input = { 2, 2 };
    res = sol.findErrorNums(input);
    cout << res[0] << " " << res[1] << endl;

    return 0;
}