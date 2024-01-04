#include <iostream>

#define MAX 47

using namespace std;

class Solution
{
public:
    int climbStairs(int n)
    {
        int n1 = 0;
        int n2 = 1;
        int n3 = 0;

        for (int i = 0; i < n; ++i)
        {
            n3 = n1 + n2;
            n1 = n2;
            n2 = n3;
        }

        return n3;
    }
};

int main()
{
    Solution a;

    cout << a.climbStairs(2) << endl;
    cout << a.climbStairs(3) << endl;

    return 0;
}