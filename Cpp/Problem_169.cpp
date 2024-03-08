#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

// Problem - 169: https://leetcode.com/problems/majority-element/
// C++ Solution!
class Solution {
public:
    // O(n) -> Space complexity
    int majorityElement_n_space(vector<int>& nums) {
        unordered_map<int, int> freq;

        for (int i : nums) {
            freq[i]++;

            if (freq[i] > (nums.size() / 2)) return i;
        }

        return -1;
    }

    // O(1) -> Space complexity [Boyer-Moore Algorithm]
    int majorityElement(vector<int>& nums) {
        int res = 0, count = 0;

        for (int i : nums) {
            if (count == 0)
                res = i;
            else if (count > (nums.size() / 2))
                return res;

            count += res == i ? 1 : -1;
        }
        return res;
    }
};

int main() {
    Solution sol;

    vector<int> input = { 3,2,3 };
    cout << sol.majorityElement(input) << endl;

    input = { 2,2,1,1,1,2,2 };
    cout << sol.majorityElement(input) << endl;

    return 0;
}