#include <string>
#include <iostream>

using namespace std;

class Solution
{
public:
    bool isPalindrome(string s)
    {
        if (s.size() == 0)
            return true;

        int front = 0, back = s.size() - 1;

        while (front <= back)
        {
            while (!isalnum(s[front]) && front < back)
            {
                ++front;
            }
            while (!isalnum(s[back]) && front < back)
            {
                --back;
            }
            s[front] = tolower(s[front]);
            s[back] = tolower(s[back]);

            if (s[front] != s[back])
            {
                return false;
            }
            ++front;
            --back;
        }

        return true;
    }
};

int main()
{
    Solution a;

    cout << a.isPalindrome("A man, a plan, a canal: Panama") << endl;
    cout << a.isPalindrome("race a car") << endl;
    cout << a.isPalindrome(" ") << endl;

    return 0;
}