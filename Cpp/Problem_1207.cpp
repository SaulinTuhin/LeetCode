#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>

using namespace std;

// Problem - 1207: https://leetcode.com/problems/unique-number-of-occurrences/
// C++ Solution!
class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        unordered_set<int> freqSet;

        for (int i = 0; i < arr.size(); i++) {
            int count = 1;

            while (i + 1 < arr.size() && arr[i] == arr[i + 1]) {
                count++;
                i++;
            }

            if (freqSet.find(count) != freqSet.end())
                return false;

            freqSet.insert(count);
        }

        return true;
    }
};

int main() {
    Solution sol;

    vector<int> input = { 1,2,2,1,1,3 };
    cout << sol.uniqueOccurrences(input) << endl;
    input = { 1, 2 };
    cout << sol.uniqueOccurrences(input) << endl;
    input = { -3,0,1,-3,1,1,1,-3,10,0 };
    cout << sol.uniqueOccurrences(input) << endl;

    return 0;
}