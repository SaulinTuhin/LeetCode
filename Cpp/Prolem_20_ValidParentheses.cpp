#include <iostream>
#include <string>
#include <stack>

using namespace std;

class Solution
{
public:
    bool isValid(string s)
    {
        stack<char> stk;

        for (int i = 0; i < s.size(); ++i)
        {
            if (s[i] == '(' || s[i] == '{' || s[i] == '[')
            {
                stk.push(s[i]);
            }
            else if (s[i] == ')')
            {
                if (stk.empty() || stk.top() != '(')
                    return false;

                stk.pop();
            }
            else if (s[i] == '}')
            {
                if (stk.empty() || stk.top() != '{')
                    return false;

                stk.pop();
            }
            else
            {
                if (stk.empty() || stk.top() != '[')
                    return false;

                stk.pop();
            }
        }
        return stk.empty();
    }
};

int main()
{
    Solution a;

    cout << a.isValid("()") << endl;
    cout << a.isValid("()[]{}") << endl;
    cout << a.isValid("(]") << endl;
    cout << a.isValid("]") << endl;

    return 0;
}