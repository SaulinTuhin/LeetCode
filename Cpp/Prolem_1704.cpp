#include <iostream>
#include <string>

using namespace std;

// Problem - 1704: https://leetcode.com/problems/determine-if-string-halves-are-alike/
// C++ Solution!
class Solution {
public:
    bool isVowel(char c) {
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U')
            return true;
        else
            return false;
    }

    bool halvesAreAlike(string s) {
        int firstCount = 0, secondCount = 0;

        for (int first = 0, second = s.size() / 2; first < s.size() / 2; first++, second++) {
            if (isVowel(s[first]))
                firstCount++;

            if (isVowel(s[second]))
                secondCount++;
        }

        return firstCount == secondCount;
    }
};

int main() {
    Solution sol;

    cout << sol.halvesAreAlike("book") << endl;
    cout << sol.halvesAreAlike("textbook") << endl;

    return 0;
}