#include <vector>
#include <unordered_map>
#include <iostream>
#include <map>

using namespace std;

class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        unordered_map<int, int> checked;

        for (int i = 0; i < nums.size(); ++i)
        {
            if (checked.find(target - nums[i]) != checked.end())
            {
                return {checked[target - nums[i]], i};
            }
            checked[nums[i]] = i;
        }

        return {-1, -1};
    }

    vector<int> twoSumJakir(vector<int> &nums, int target)
    {
        vector<int> ans;
        map<int, int> m;
        for (int i = 0; i < nums.size(); i++)
        {
            if (m.find(target - nums[i]) != m.end())
            {
                ans.push_back(m[target - nums[i]]);
                ans.push_back(i);
                return ans;
            }
            m[nums[i]] = i;
        }
        return ans;
    }

    vector<int> twoSum(vector<int> &nums, int target)
    {
        int sum = 0;
        vector<int> result;
        for (int i = 0; i < nums.size(); i++)
        {
            for (int j = 0; j < nums.size(); j++)
            {
                if (i == j)
                    continue;
                sum = nums[i] + nums[j];
                if (sum == target)
                {
                    result.push_back(i);
                    result.push_back(j);
                    return result;
                }
            }
        }
        return result;
    }
};

int main()
{
    Solution a;

    vector<int> in = {2, 7, 11, 15};

    vector<int> res = a.twoSum(in, 9);

    cout << res[0] << " " << res[1] << endl;

    return 0;
}