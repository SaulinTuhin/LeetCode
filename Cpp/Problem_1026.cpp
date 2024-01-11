#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
};

// Problem - 1026: https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
// C++ Solution!
class Solution {
public:
    int maxDiff = 0;

    pair<int, int> dfs(TreeNode* root) {
        if (!root)
            return { INT_MAX, INT_MIN };

        pair<int, int> left = dfs(root->left);
        pair<int, int> right = dfs(root->right);

        int minVal = min(left.first, right.first);
        int maxVal = max(left.second, right.second);

        if (root->left || root->right)
            maxDiff = max({ maxDiff, abs(root->val - minVal), abs(root->val - maxVal) });

        return { min(root->val, minVal), max(root->val, maxVal) };
    }

    int maxAncestorDiff(TreeNode* root) {
        maxDiff = 0;

        dfs(root);

        return maxDiff;
    }

    TreeNode* makeTree(vector<int>& nums, int i) {
        if (i >= nums.size() || !nums[i])
            return nullptr;

        TreeNode* root = new TreeNode(nums[i]);
        root->left = makeTree(nums, i * 2 + 1);
        root->right = makeTree(nums, i * 2 + 2);

        return root;
    }
};

int main() {
    Solution sol;

    vector<int> input = { 8,3,10,1,6,NULL,14,NULL,NULL,4,7,13 };
    cout << sol.maxAncestorDiff(sol.makeTree(input, 0)) << endl;
    input = { 1,NULL,2,NULL,0,3 };
    cout << sol.maxAncestorDiff(sol.makeTree(input, 0)) << endl;

    return 0;
}