#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

// Problem - 2225: https://leetcode.com/problems/find-players-with-zero-or-one-losses/
// C++ Solution!
class Solution {
public:
    vector<vector<int>> findWinners(vector<vector<int>>& matches) {
        unordered_map<int, int> lossCount;
        unordered_set<int> winners;
        unordered_set<int> oneLoss;

        for (int i = 0; i < matches.size(); i++) {
            int winner = matches[i][0];
            int loser = matches[i][1];

            lossCount[loser]++;

            if (lossCount[loser] == 1) {
                winners.erase(loser);
                oneLoss.insert(loser);
            }
            else if (lossCount[loser] == 2) {
                oneLoss.erase(loser);
            }

            if (lossCount.find(winner) == lossCount.end()) {
                winners.insert(winner);
            }
        }

        vector<int> resWinners(winners.begin(), winners.end());
        vector<int> resOneLoss(oneLoss.begin(), oneLoss.end());

        sort(resWinners.begin(), resWinners.end());
        sort(resOneLoss.begin(), resOneLoss.end());

        return { resWinners, resOneLoss };
    }

    void printSol(vector<vector<int>> input) {
        for (vector<int> inputLists : input) {
            for (int input : inputLists) {
                cout << input << " ";
            }
            cout << endl;
        }
    }
};

int main() {
    Solution sol;

    vector<vector<int>> input = { {1,3},{2,3},{3,6},{5,6},{5,7},{4,5},{4,8},{4,9},{10,4},{10,9} };
    sol.printSol(sol.findWinners(input));
    input = { {2,3},{1,3},{5,4},{6,4} };
    sol.printSol(sol.findWinners(input));

    return 0;
}