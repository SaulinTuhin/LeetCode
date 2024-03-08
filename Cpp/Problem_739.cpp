#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> res(temperatures.size(), 0);
        vector<int> stack;

        for (int i = temperatures.size() - 1; i >= 0; --i) {
            int currTemperature = temperatures[i];

            while (!stack.empty() && currTemperature >= temperatures[stack.back()]) {
                stack.pop_back();
            }

            if (!stack.empty()) {
                res[i] = stack.back() - i;
            }

            stack.push_back(i);
        }

        return res;
    }
};


int main() {
    Solution sol;

    vector<int> input = { 73,74,75,71,69,72,76,73 };
    vector<int> res = sol.dailyTemperatures(input);
    for (int i : res) {
        cout << i << " ";
    }
    cout << endl << endl;

    input = { 30,40,50,60 };
    res = sol.dailyTemperatures(input);
    for (int i : res) {
        cout << i << " ";
    }
    cout << endl << endl;

    input = { 30,60,90 };
    res = sol.dailyTemperatures(input);
    for (int i : res) {
        cout << i << " ";
    }
    cout << endl << endl;

    return 0;
}