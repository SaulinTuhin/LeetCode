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

// Problem - 2807: https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/
// C++ Solution!
class Solution {
public:
	int gcd(int a, int b) {
		while (b > 0) {
			int temp = b;
			b = a % b;
			a = temp;
		}

		return a;
	}

	ListNode* insertGreatestCommonDivisors(ListNode* head) {
		ListNode* cur = head;
		while (cur->next) {
			cur->next = new ListNode(gcd(cur->val, cur->next->val), cur->next);
			cur = cur->next->next;
		}

		return head;
	}
};

int main() {
	Solution sol;

	vector<int> input = { 18, 6, 10, 3 };
	ListNode* head = nullptr;
	for (int i = input.size() - 1; i >= 0; i--) {
		head = new ListNode(input[i], head);
	}
	ListNode* cur = sol.insertGreatestCommonDivisors(head);
	while (cur) {
		cout << cur->val << " ";
		cur = cur->next;
	}
	cout << endl;

	input = { 7 };
	head = nullptr;
	for (int i = input.size() - 1; i >= 0; i--) {
		head = new ListNode(input[i], head);
	}
	cur = sol.insertGreatestCommonDivisors(head);
	while (cur) {
		cout << cur->val << " ";
		cur = cur->next;
	}
	cout << endl;

	return 0;
}