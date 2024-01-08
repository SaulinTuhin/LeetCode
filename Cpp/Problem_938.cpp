#include <iostream>
#include <vector>

using namespace std;

struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode() : val(0), left(nullptr), right(nullptr) {}
	TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
	TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

// Problem - 938: https://leetcode.com/problems/range-sum-of-bst/
// C++ Solution!
class Solution {
public:
	int rangeSumBST(TreeNode* root, int low, int high) {
		if (!root)
			return 0;

		if (root->val < low)
			return rangeSumBST(root->right, low, high);
		if (root->val > high)
			return rangeSumBST(root->left, low, high);

		return root->val + rangeSumBST(root->left, low, high) + rangeSumBST(root->right, low, high);
	}

	TreeNode* makeBST(vector<int> &input, int i) {
		if (i >= input.size() || input[i] == NULL)
			return nullptr;

		TreeNode* root = new TreeNode(input[i]);
		root->left = makeBST(input, i * 2 + 1);
		root->right = makeBST(input, i * 2 + 2);

		return root;
	}
};

int main() {
	Solution sol;
	
	vector<int> input = { 10, 5, 15, 3, 7, NULL, 18 };
	TreeNode* root = sol.makeBST(input, 0);
	cout << sol.rangeSumBST(root, 7, 15) << endl;

	input = { 10, 5, 15, 3, 7, 13, 18, 1, NULL, 6 };
	root = sol.makeBST(input, 0);
	cout << sol.rangeSumBST(root, 6, 10) << endl;

	return 0;
}