#include <iostream>
#include <vector>

using namespace std;

struct ListNode {
	int val;
	ListNode *next;
	ListNode() : val(0), next(nullptr) {}
	ListNode(int x) : val(x), next(nullptr) {}
	ListNode(int x, ListNode *next) : val(x), next(next) {}
};

// Problem - 143: https://leetcode.com/problems/reorder-list/
// C++ Solution!
class Solution {
public:
	void reorderList(ListNode* head) {
		ListNode* slow = head, *fast = head->next;

		while (fast && fast->next) {
			slow = slow->next;
			fast = fast->next->next;
		}

		ListNode* second = slow->next, *prev = nullptr;
		slow->next = nullptr;
		while (second) {
			ListNode* tmp = second->next;
			second->next = prev;

			prev = second;
			second = tmp;
		}

		ListNode* first = head;
		second = prev;
		while (second) {
			ListNode* tmp1 = first->next, *tmp2 = second->next;
			first->next = second;
			second->next = tmp1;

			first = tmp1, second = tmp2;
		}
	}
};

ListNode* createList(vector<int> in) {
	ListNode* head = new ListNode(in[0]);
	ListNode* cur = head;
	for (int i = 1; i < in.size(); i++) {
		cur->next = new ListNode(in[i]);
		cur = cur->next;
	}

	return head;
}

void printRes(ListNode* head) {
	while (head) {
		cout << head->val << "->";
		head = head->next;
	}
	cout << endl;
}

int main() {
	Solution sol;

	ListNode* in_head = createList({ 1,2,3,4 });
	sol.reorderList(in_head);
	printRes(in_head);

	in_head = createList({ 1,2,3,4,5 });
	sol.reorderList(in_head);
	printRes(in_head);

	return 0;
}