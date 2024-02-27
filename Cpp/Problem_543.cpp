#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode() : val(0), left(nullptr), right(nullptr) {}
	TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
	TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

// Problem - 543: https://leetcode.com/problems/diameter-of-binary-tree/
// C++ Solution!
class Solution {
public:
	int dfs(TreeNode* root, int& res) {
		if (!root)
			return 0;

		int left = dfs(root->left, res);
		int right = dfs(root->right, res);
		res = max(res, left + right);

		return 1 + max(left, right);
	}

	int diameterOfBinaryTree(TreeNode* root) {
		int res = 0;

		dfs(root, res);

		return res;
	}
};

TreeNode* createTree(vector<int>& nums, int i) {
	if (i >= nums.size() || !nums[i])
		return nullptr;

	TreeNode* root = new TreeNode(nums[i]);
	root->left = createTree(nums, i * 2 + 1);
	root->right = createTree(nums, i * 2 + 2);

	return root;
}

int main() {
	Solution sol;

	vector<int> input = { 1, 2, 3, 4, 5 };
	cout << sol.diameterOfBinaryTree(createTree(input, 0)) << endl;

	input = { 1, 2 };
	cout << sol.diameterOfBinaryTree(createTree(input, 0)) << endl;

	return 0;
}