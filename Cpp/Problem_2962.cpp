#include <iostream>
#include <vector>

using namespace std;

// Problem - 2962: https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/
// C++ Solution!
class Solution {
public:
    long long countSubarrays(vector<int>& nums, int k) {
        int max = *max_element(nums.begin(), nums.end());
        int current_count = 0;

        int left = 0;
        long long res = 0;
        for (int right = 0; right < nums.size(); right++) {
            if (nums[right] == max)
                current_count++;

            while (current_count == k) {
                if (nums[left] == max)
                    current_count--;

                left++;
            }

            res += left;
        }

        return res;
    }
};

int main() {
    Solution sol;

    vector<int> input = { 1,3,2,3,3 };
    cout << sol.countSubarrays(input, 2) << endl;

    input = { 1,4,2,1 };
    cout << sol.countSubarrays(input, 3) << endl;

    return 0;
}