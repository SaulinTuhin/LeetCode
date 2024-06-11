#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

// Problem - 992: Subarrays with K Different Integers
// C++ Solution!
class Solution {
public:
    int subarraysWithKDistinct(vector<int>& nums, int k) {
        int res = 0, left = 0, middle = 0;
        unordered_map<int, int> count;

        for (int right = 0; right < nums.size(); right++) {
            count[nums[right]]++;

            while (count.size() > k) {
                count[nums[middle]]--;
                if (count[nums[middle]] == 0)
                    count.erase(nums[middle]);

                middle++;
                left = middle;
            }

            while (count[nums[middle]] > 1) {
                count[nums[middle]]--;
                middle++;
            }

            if (count.size() == k)
                res += middle - left + 1;
        }

        return res;
    }
};

int main() {
    Solution sol;

    vector<int> input = { 1,2,1,2,3 };
    cout << sol.subarraysWithKDistinct(input, 2) << endl;

    input = { 1,2,1,3,4 };
    cout << sol.subarraysWithKDistinct(input, 3) << endl;

    return 0;
}