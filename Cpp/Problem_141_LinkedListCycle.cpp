#include <iostream>

using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution
{
public:
    bool hasCycle(ListNode *head)
    {
        if (!head)
            return false;

        ListNode *fast = head;

        while (fast && fast->next)
        {
            head = head->next;
            fast = fast->next->next;

            if (head == fast)
                return true;
        }

        return false;
    }
};

int main()
{
    Solution a;

    ListNode *in;

    cout << a.hasCycle(in) << endl;

    return 0;
}