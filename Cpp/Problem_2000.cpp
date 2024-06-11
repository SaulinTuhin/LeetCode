#include <iostream>
#include <string>

using namespace std;

// Problem - 2000: https://leetcode.com/problems/reverse-prefix-of-word/
// C++ Solution!
class Solution {
public:
    string reversePrefix(string word, char ch) {
        int i = word.find(ch);
        reverse(word.begin(), word.begin() + i + 1);
        return word;
    }
};

int main() {
    Solution sol;

    cout << sol.reversePrefix("abcdefd", 'd') << endl;
    cout << sol.reversePrefix("xyxzxe", 'z') << endl;
    cout << sol.reversePrefix("abcd", 'z') << endl;

    return 0;
}