#include <cstdint>
#include <iostream>

using namespace std;

class Solution
{
public:
    int hammingWeight(uint32_t n)
    {
        return n == 0 ? 0 : (n & 1) + hammingWeight(n >> 1);
    }

    int hammingWeight(uint32_t n)
    {
        if (n == 0)
            return 0;

        return (n & 1) + hammingWeight(n >> 1);
    }
};

int main()
{
    Solution a;

    cout << a.hammingWeight(00000000000000000000000000001011) << endl;

    return 0;
}