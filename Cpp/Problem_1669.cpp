#include <iostream>
#include <vector>

using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};

// Problem - 1669: https://leetcode.com/problems/merge-in-between-linked-lists/
// C++ Solution!
class Solution {
public:
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        ListNode* start = list1;

        int i = 0;
        while (i < a - 1) {
            start = start->next;
            i++;
        }

        ListNode* end = start;
        while (i <= b) {
            end = end->next;
            i++;
        }

        start->next = list2;
        while (list2->next)
            list2 = list2->next;

        list2->next = end;

        return list1;
    }
};

ListNode* makeList(vector<int>& list) {
    ListNode* head = new ListNode(list[0]);

    ListNode* temp = head;
    for (int i = 1; i < list.size(); i++) {
        temp->next = new ListNode(list[i]);
        temp = temp->next;
    }

    return head;
}

void printRes(ListNode* head) {
    while (head) {
        cout << head->val << ',';
        head = head->next;
    }

    cout << endl;
}

int main() {
    Solution sol;

    vector<int> list1 = { 10,1,13,6,9,5 }, list2 = { 1000000,1000001,1000002 };
    printRes(sol.mergeInBetween(makeList(list1), 3, 4, makeList(list2)));

    list1 = { 0,1,2,3,4,5,6 }, list2 = { 1000000,1000001,1000002,1000003,1000004 };
    printRes(sol.mergeInBetween(makeList(list1), 2, 5, makeList(list2)));

    return 0;
}