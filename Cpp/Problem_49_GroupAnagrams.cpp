#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>

using namespace std;

class Solution
{
public:
    vector<vector<string>> groupAnagrams(vector<string> &strs)
    {
        unordered_map<string, vector<string>> anagramMap;

        for (string str : strs)
        {
            int count[26] = {0};
            for (int i = 0; i != str.size(); ++i)
            {
                count[str[i] - 'a']++;
            }

            string hash = "";
            for (int i = 0; i < 26; ++i)
            {
                hash.append(string(1, 'a' + i));
                hash.append(to_string(count[i]));
            }

            anagramMap[hash].push_back(str);
        }

        vector<vector<string>> result;

        for (auto i : anagramMap)
        {
            result.push_back(i.second);
        }

        return result;
    }
};

int main()
{
    Solution a;

    vector<string> in{"eat", "tea", "tan", "ate", "nat", "bat"};

    vector<vector<string>> out = a.groupAnagrams(in);

    return 0;
}