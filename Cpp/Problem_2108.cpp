#include <iostream>
#include <vector>
#include <string>

using namespace std;

// Problem - 2108: https://leetcode.com/problems/find-first-palindromic-string-in-the-array/
// C++ Solution!
class Solution {
public:
    string firstPalindrome(vector<string>& words) {
        for (string str : words) {
            int left = 0, right = str.size() - 1;

            while (left < right) {
                if (str[left] != str[right]) {
                    break;
                }

                left++;
                right--;
            }

            if (left >= right)
                return str;
        }

        return "";
    }
};

int main() {
    Solution sol;

    vector<string> input = { "abc","car","ada","racecar","cool" };
    cout << sol.firstPalindrome(input) << endl;

    input = { "notapalindrome","racecar" };
    cout << sol.firstPalindrome(input) << endl;

    input = { "def","ghi" };
    cout << sol.firstPalindrome(input) << endl;

    return 0;
}