#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

class Solution
{
public:
    bool containsDuplicate(vector<int> &nums)
    {
        unordered_set<int> hash;

        for (int i = 0; i < nums.size(); ++i)
        {
            if (hash.find(nums[i]) != hash.end())
            {
                return true;
            }
            hash.insert(nums[i]);
        }
        return false;
    }
};

int main()
{
    Solution a;
    vector<int> in = {1, 2, 3, 1};

    cout << a.containsDuplicate(in) << endl;

    return 0;
}