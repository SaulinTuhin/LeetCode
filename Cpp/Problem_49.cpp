#include <iostream>
#include <vector>
#include <sstream>
#include <unordered_map>

using namespace std;

// Problem - 49: https://leetcode.com/problems/group-anagrams/
// C++ Solution!
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> anagramMap;

        for (string str : strs) {
            vector<int> count(26, 0);
            for (char i : str) count[i - 'a']++;

            stringstream hash;
            for (int i = 0; i < 26; i++) hash << (char)(i + 'a') << count[i];

            anagramMap[hash.str()].push_back(str);
        }

        vector<vector<string>> res;
        for (auto i : anagramMap) {
            res.push_back(i.second);
        }

        return res;
    }
};

void printOutput(vector<vector<string>> res) {
    cout << "[";
    for (vector<string> i : res) {
        cout << "[\"";
        for (string j : i) {
            cout << j << ", ";
        }
        cout << "\"],";
    }
    cout << "]" << endl;
}

int main() {
    Solution sol;

    vector<string> input = { "eat","tea","tan","ate","nat","bat" };
    vector<vector<string>> res = sol.groupAnagrams(input);
    printOutput(res);

    input = { "" };
    res = sol.groupAnagrams(input);
    printOutput(res);

    input = { "a" };
    res = sol.groupAnagrams(input);
    printOutput(res);

    return 0;
}