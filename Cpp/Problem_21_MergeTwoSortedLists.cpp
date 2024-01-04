#include <iostream>

using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution
{
public:
    ListNode *mergeTwoLists(ListNode *list1, ListNode *list2)
    {
        if (!list1)
            return list2;

        if (!list2)
            return list1;

        ListNode *res = list1;
        if (list2->val < list1->val)
        {
            res = list2;
            list2 = list2->next;
        }
        else
        {
            list1 = list1->next;
        }

        ListNode *cur = res;
        while (list1 && list2)
        {
            if (list1->val < list2->val)
            {
                cur->next = list1;
                list1 = list1->next;
            }
            else
            {
                cur->next = list2;
                list2 = list2->next;
            }
            cur = cur->next;
        }

        if (!list1)
            cur->next = list2;
        else
            cur->next = list1;

        return res;
    }
};

int main()
{
    Solution a;

    ListNode *in1;

    ListNode *in2;

    ListNode *res = a.mergeTwoLists(in1, in2);

    return 0;
}