#include <string>
#include <iostream>
#include <map>

using namespace std;

class Solution
{
public:
    bool isAnagram(string s, string t)
    {
        if (s.size() != t.size())
            return false;

        int res[26] = {0};
        int chk = 0;
        for (int i = 0; i < s.size(); ++i)
        {
            int a = s[i] - 'a';
            int b = t[i] - 'a';

            ++res[a] <= 0 ? --chk : ++chk;
            --res[b] >= 0 ? --chk : ++chk;
        }

        return !chk;
    }

    bool isAnagramJakir(string s, string t)
    {
        int arr[26] = {0};
        if (s.length() != t.length())
            return false;
        for (int i = 0; i < s.length(); ++i)
            ++arr[s[i] - 'a'];
        for (int i = 0; i < t.length(); ++i)
        {
            if (arr[t[i] - 'a'] == 0)
                return false;
            --arr[t[i] - 'a'];
        }
        return true;
    }

    bool isAnagramJoy(string s, string t)
    {
        map<char, int> hash_map;
        for (int i = 0; i < s.size(); i++)
        {
            hash_map[s[i]]++;
        }
        for (int j = 0; j < t.size(); j++)
        {
            hash_map[t[j]]--;
        }
        for (auto x : hash_map)
        {
            if (x.second != 0)
            {
                return false;
            }
        }
        return true;
    }
};

int main()
{
    Solution a;

    cout << "Output: " << a.isAnagramJoy("anagram", "nagaram") << endl;
    cout << "Output: " << a.isAnagramJoy("yqhbicoumu", "ouiuycbmqh") << endl;
    cout << "Output: " << a.isAnagramJoy("rat", "car") << endl;
    cout << "Output: " << a.isAnagramJoy("ac", "bb") << endl;

    return 0;
}