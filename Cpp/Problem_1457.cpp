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

// Problem - 1457: https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/
// C++ Solution!
class Solution {
public:
    int pseudoPalindromicPaths(TreeNode* root) {
        vector<int> freq(10, 0);

        return dfs(root, freq, 0);
    }

    int dfs(TreeNode* cur, vector<int>& freq, int oddCount) {
        if (!cur)
            return 0;

        freq[cur->val]++;
        if (freq[cur->val] % 2)
            oddCount++;
        else
            oddCount--;

        int res = 0;
        if (!cur->left && !cur->right)
            res = oddCount <= 1 ? 1 : 0;
        else
            res = dfs(cur->left, freq, oddCount) + dfs(cur->right, freq, oddCount);

        freq[cur->val]--;
        return res;
    }
};

TreeNode* createTree(vector<int>& nums, int i) {
    if (i >= nums.size() || !nums[i])
        return nullptr;

    TreeNode* root = new TreeNode(nums[i]);
    root->left = new TreeNode(nums[i * 2 + 1]);
    root->right = new TreeNode(nums[i * 2 + 2]);

    return root;
}

int main() {
    Solution sol;

    vector<int> input = { 2,3,1,3,1,NULL,1 };
    cout << sol.pseudoPalindromicPaths(createTree(input, 0)) << endl;
    input = { 2,1,1,1,3,NULL,NULL,NULL,NULL,NULL,1 };
    cout << sol.pseudoPalindromicPaths(createTree(input, 0)) << endl;
    input = { 9 };
    cout << sol.pseudoPalindromicPaths(createTree(input, 0)) << endl;

    return 0;
}