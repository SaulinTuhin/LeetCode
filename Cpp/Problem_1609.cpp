#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
};

// Problem - 1609: https://leetcode.com/problems/even-odd-tree/
// C++ Solution!
class Solution {
public:
    bool isEvenOddTree(TreeNode* root) {
        if (!root)
            return true;

        bool isEven = true;
        queue<TreeNode*> q;
        q.push(root);

        while (!q.empty()) {
            int prev = isEven ? INT_MIN : INT_MAX;

            int lCount = q.size();
            for (int i = 0; i < lCount; i++) {
                TreeNode* cur = q.front();
                q.pop();

                if (isEven && (cur->val % 2 == 0 || cur->val <= prev))
                    return false;
                else if (!isEven && (cur->val % 2 == 1 || cur->val >= prev))
                    return false;

                if (cur->left) q.push(cur->left);
                if (cur->right) q.push(cur->right);
                prev = cur->val;
            }
            isEven = !isEven;
        }

        return true;
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

    vector<int> input = { 1,10,4,3,NULL,7,9,12,8,6,NULL,NULL,2 };
    cout << sol.isEvenOddTree(createTree(input, 0)) << endl;

    input = { 5,4,2,3,3,7 };
    cout << sol.isEvenOddTree(createTree(input, 0)) << endl;

    input = { 5,9,1,3,5,7 };
    cout << sol.isEvenOddTree(createTree(input, 0)) << endl;

    return 0;
}