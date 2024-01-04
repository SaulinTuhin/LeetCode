#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    int maxProduct(vector<int> &nums)
    {
        sort(nums.begin(), nums.end());

        return (nums[nums.size() - 1] - 1) * (nums[nums.size() - 2] - 1);
    }
};

int main()
{
    Solution sol;

    vector<int> input1 = {3, 4, 5, 2};
    vector<int> input2 = {1, 5, 4, 5};
    vector<int> input3 = {3, 7};

    int output = sol.maxProduct(input3);

    cout << output << endl;

    return 0;
}