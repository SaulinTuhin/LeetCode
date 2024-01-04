#include <vector>
#include <iostream>

using namespace std;

class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        int max_profit = 0, lowest_price = INT_MAX;
        for (int i = 0; i < prices.size(); ++i)
        {
            if (prices[i] < lowest_price)
                lowest_price = prices[i];
            else if (prices[i] - lowest_price > max_profit)
                max_profit = prices[i] - lowest_price;
        }

        return max_profit;
    }
};

int main()
{
    Solution a;

    vector<int> in = {1, 2};
    vector<int> in1 = {7, 6, 4, 3, 1};

    cout << a.maxProfit(in) << endl;
    cout << a.maxProfit(in1) << endl;

    return 0;
}