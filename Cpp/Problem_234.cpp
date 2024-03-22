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

// Problem - 234: https://leetcode.com/problems/palindrome-linked-list/
// C++ Solution!
class Solution {
public:
    // O(N) - Time | O(N) - Memory
    bool isPalindrome_normal(ListNode* head) {
        vector<int> list;

        while (head) {
            list.push_back(head->val);

            head = head->next;
        }

        int l = 0, r = list.size() - 1;
        while (l <= r) {
            if (list[l] != list[r])
                return false;

            l++;
            r--;
        }

        return true;
    }

    // O(N) - Time | O(1) - Memory
    bool isPalindrome(ListNode* head) {
        ListNode* slow = head, * fast = head;

        while (fast && fast->next) {
            fast = fast->next->next;
            slow = slow->next;
        }

        ListNode* prev = nullptr;
        while (slow) {
            ListNode* temp = slow->next;
            slow->next = prev;

            prev = slow;
            slow = temp;
        }

        while (prev) {
            if (head->val != prev->val)
                return false;

            head = head->next;
            prev = prev->next;
        }

        return true;
    }
};

ListNode* createList(vector<int> input) {
    ListNode* head = new ListNode(input[0]);
    ListNode* tmp = head;
    for (int i = 1; i < input.size(); i++) {
        tmp->next = new ListNode(input[i]);
        tmp = tmp->next;
    }

    return head;
}

int main() {
    Solution sol;

    cout << sol.isPalindrome(createList({ 1,2,2,1 })) << endl;

    cout << sol.isPalindrome(createList({ 1,2 })) << endl;

    return 0;
}