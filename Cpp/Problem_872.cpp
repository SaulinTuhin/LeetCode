#include <iostream>
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

// Problem - 872: https://leetcode.com/problems/leaf-similar-trees/
// C++ Solution!
class Solution {
public:
    void dfs(TreeNode* root, vector<int>& leafs) {
        if (!root)
            return;
        if (!root->left && !root->right) {
            leafs.push_back(root->val);
            return;
        }

        dfs(root->left, leafs);
        dfs(root->right, leafs);
    }

    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        vector<int> leafs1, leafs2;
        dfs(root1, leafs1);
        dfs(root2, leafs2);

        return leafs1 == leafs2;
    }

    TreeNode* createTree(vector<int>& nums, int i) {
        if (i >= nums.size() || !nums[i])
            return nullptr;

        TreeNode* root = new TreeNode(nums[i]);
        root->left = new TreeNode(nums[i * 2 + 1]);
        root->right = new TreeNode(nums[i * 2 + 2]);

        return root;
    }
};

int main() {
    Solution sol;

    vector<int> input = { 3,5,1,6,2,9,8,NULL,NULL,7,4 };
    TreeNode* root1 = sol.createTree(input, 0);
    input = { 3,5,1,6,7,4,2,NULL,NULL,NULL,NULL,NULL,NULL,9,8 };
    TreeNode* root2 = sol.createTree(input, 0);
    cout << sol.leafSimilar(root1, root2) << endl;

    input = { 1,2,3 };
    root1 = sol.createTree(input, 0);
    input = { 1,3,2 };
    root2 = sol.createTree(input, 0);
    cout << sol.leafSimilar(root1, root2) << endl;

    return 0;
}