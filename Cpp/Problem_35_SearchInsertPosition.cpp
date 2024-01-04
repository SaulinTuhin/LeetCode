#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

class Solution
{
public:
    int searchInsert(vector<int> &nums, int target)
    {
        return lower_bound(nums.begin(), nums.end(), target) - nums.begin();
    }

    int searchInsertBS(vector<int> &nums, int target)
    {
        int left = 0, right = nums.size() - 1, mid = 0;

        while (left <= right)
        {
            mid = left + (right - left) / 2;

            if (nums[mid] < target)
            {
                left = mid + 1;
            }
            else if (nums[mid] > target)
            {
                right = mid - 1;
            }
            else
                return mid;
        }
        return left;
    }
};

int main()
{
    Solution a;
    vector<int> in = {1, 3, 5, 6};
    cout << a.searchInsertBS(in, 7) << endl;
    vector<int> in1 = {1, 3, 5, 6};
    cout << a.searchInsertBS(in1, 0) << endl;

    return 0;
}