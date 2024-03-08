#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>

using namespace std;

// Problem - 2092: https://leetcode.com/problems/find-all-people-with-secret/
// C++ Solution!
class Solution {
public:
    void dfs(int src, unordered_map<int, vector<int>>& adj, unordered_set<int>& visited, unordered_set<int>& withSecrets) {
        if (visited.find(src) != visited.end())
            return;

        visited.insert(src);
        withSecrets.insert(src);

        for (int neighbor : adj[src]) {
            dfs(neighbor, adj, visited, withSecrets);
        }
    }

    vector<int> findAllPeople(int n, vector<vector<int>>& meetings, int firstPerson) {
        unordered_set<int> withSecret = { 0, firstPerson };
        map<int, unordered_map<int, vector<int>>> timeMap;

        for (vector<int> meet : meetings) {
            timeMap[meet[2]][meet[0]].push_back(meet[1]);
            timeMap[meet[2]][meet[1]].push_back(meet[0]);
        }

        for (auto time : timeMap) {
            unordered_set<int> visited;
            for (auto src : timeMap[time.first]) {
                if (withSecret.find(src.first) != withSecret.end()) {
                    dfs(src.first, timeMap[time.first], visited, withSecret);
                }
            }
        }

        vector<int> res(withSecret.begin(), withSecret.end());
        return res;
    }
};

void printRes(vector<int>& res) {
    for (int i : res) {
        cout << i << " ";
    }
    cout << endl << endl;
}

int main() {
    Solution sol;

    vector<vector<int>> input = { {1,2,5},{2,3,8},{1,5,10} };
    vector<int> res = sol.findAllPeople(6, input, 1);
    printRes(res);

    input = { {3,1,3},{1,2,2},{0,3,3} };
    res = sol.findAllPeople(4, input, 3);
    printRes(res);

    input = { {3,4,2},{1,2,1},{2,3,1} };
    res = sol.findAllPeople(5, input, 1);
    printRes(res);

    return 0;
}