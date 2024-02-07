#include <iostream>
#include <string>
#include <unordered_map>
#include <sstream>
#include <queue>
#include <set>

using namespace std;

// Problem - 451: https://leetcode.com/problems/sort-characters-by-frequency/
// C++ Solution!
class Solution {
public:
    string frequencySort(string s) {
        unordered_map<char, int> freq;
        for (char i : s) freq[i]++;

        // using unordered map
        /*
        unordered_map<int, string> counts;
        for (auto i : freq) {
            counts[i.second].push_back(i.first);
        }

        stringstream res;
        for (int i = s.size(); i > 0; i--) {
            for (char c : counts[i]) {
                for (int j = 0; j < i; j++) {
                    res << c;
                }
            }
        }
        */

        // using priority queue
        priority_queue<pair<int, char>> pq;
        for (auto i : freq) pq.push({ i.second, i.first });

        stringstream res;
        while (!pq.empty()) {
            int count = pq.top().first;
            while (count--)
            {
                res << pq.top().second;
            }
            pq.pop();
        }

        // using set
        /*
        set<pair<int, char>, greater<pair<int, char>>> pq;
        for (auto i : freq) pq.insert({ i.second, i.first });

        stringstream res;

        for (auto i : pq) {
            int count = i.first;

            while (count--) {
                res << i.second;
            }
        }
        */

        return res.str();
    }
};

int main() {
    Solution sol;

    cout << sol.frequencySort("tree") << endl;
    cout << sol.frequencySort("cccaaa") << endl;
    cout << sol.frequencySort("Aabb") << endl;

    return 0;
}