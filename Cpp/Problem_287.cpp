#include <iostream>
#include <vector>

using namespace std;

// Problem - 287: https://leetcode.com/problems/find-the-duplicate-number/
// C++ Solution!
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int slow = 0, fast = 0;
        do
        {
            slow = nums[slow];
            fast = nums[nums[fast]];
        } while (slow != fast);

        int slow2 = 0;
        do
        {
            slow = nums[slow];
            slow2 = nums[slow2];
        } while (slow != slow2);

        return slow;
    }
};

int main() {
    Solution sol;

    vector<int> input = { 1,3,4,2,2 };
    cout << sol.findDuplicate(input) << endl;

    input = { 3,1,3,4,2 };
    cout << sol.findDuplicate(input) << endl;

    input = { 3,3,3,3,3 };
    cout << sol.findDuplicate(input) << endl;

    return 0;
}