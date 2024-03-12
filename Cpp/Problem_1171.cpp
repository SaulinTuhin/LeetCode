#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

struct ListNode {
	int val;
	ListNode *next;
	ListNode() : val(0), next(nullptr) {}
	ListNode(int x) : val(x), next(nullptr) {}
	ListNode(int x, ListNode *next) : val(x), next(next) {}
};

// Problem - 1171: https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/
// C++ Solution!
class Solution {
public:
	ListNode* removeZeroSumSublists(ListNode* head) {
		ListNode node = ListNode(0, head);
		unordered_map<int, ListNode*> prefixSums;

		ListNode* temp = &node;
		int curSum = 0;
		while (temp) {
			curSum += temp->val;
			prefixSums[curSum] = temp;

			temp = temp->next;
		}

		curSum = 0;
		temp = &node;
		while (temp) {
			curSum += temp->val;
			temp->next = prefixSums[curSum]->next;

			temp = temp->next;
		}

		return node.next;
	}
};

ListNode* createTree(vector<int> input) {
	ListNode* head = new ListNode(input[input.size() - 1]);
	for (int i = input.size() - 2; i >= 0; i--) {
		ListNode* temp = new ListNode(input[i]);
		temp->next = head;
		
		head = temp;
	}

	return head;
}

void printRes(ListNode* res) {
	while (res->next) {
		cout << res->val << ",";

		res = res->next;
	}
	cout << res->val << endl;
}

int main() {
	Solution sol;

	vector<int> input = { 1, 2, -3, 3, 1 };
	printRes(sol.removeZeroSumSublists(createTree(input)));

	input = { 1, 2, 3, -3, 4 };
	printRes(sol.removeZeroSumSublists(createTree(input)));

	input = { 1, 2, 3, -3, -2 };
	printRes(sol.removeZeroSumSublists(createTree(input)));

	return 0;
}