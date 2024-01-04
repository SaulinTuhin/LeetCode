#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution
{
public:
    int minOperations(vector<int> &nums)
    {
        unordered_map<int, int> counts;

        for (int num : nums)
        {
            counts[num]++;
        }

        int res = 0;
        for (auto count : counts)
        {
            if (count.second % 3 == 0)
            {
                res += count.second / 3;
                count.second %= 3;
            }
            if (count.second % 2 == 0)
            {
                res += count.second / 2;
                count.second %= 2;
            }
        }

        return res == 0 ? -1 : res;
    }
};

int main()
{
    Solution sol;

    vector<int> input = {2, 3, 3, 2, 2, 4, 2, 3, 4};
    cout << sol.minOperations(input) << endl;
    input = {2, 1, 2, 2, 3, 3};
    cout << sol.minOperations(input) << endl;

    return 0;
}