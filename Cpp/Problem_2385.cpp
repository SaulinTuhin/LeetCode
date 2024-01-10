#include <iostream>
#include <unordered_map>
#include <unordered_set>
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

// Problem - 2385: https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/
// C++ Solution!
class Solution {
public:
    int amountOfTime(TreeNode* root, int start) {
        unordered_map<int, vector<int>> adjMatrix;
        makeAdjMatrix(root, adjMatrix);

        queue<int> q;
        q.push(start);
        unordered_set<int> visited;

        int minPassed = -1;
        while (!q.empty()) {
            minPassed++;
            for (int adjCount = q.size(); adjCount > 0; adjCount--) {
                int cur = q.front();
                q.pop();
                for (int adj : adjMatrix[cur]) {
                    if (!visited.count(adj))
                        q.push(adj);
                }
                visited.insert(cur);
            }
        }

        return minPassed;
    }

    void makeAdjMatrix(TreeNode* root, unordered_map<int, vector<int>>& adjMatrix) {
        if (!root)
            return;

        if (root->left) {
            adjMatrix[root->val].push_back(root->left->val);
            adjMatrix[root->left->val].push_back(root->val);
        }
        if (root->right) {
            adjMatrix[root->val].push_back(root->right->val);
            adjMatrix[root->right->val].push_back(root->val);
        }

        makeAdjMatrix(root->left, adjMatrix);
        makeAdjMatrix(root->right, adjMatrix);
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

    vector<int> input = { 1,5,3,NULL,4,10,6,9,2 };
    cout << sol.amountOfTime(sol.createTree(input, 0), 3) << endl;
    input = { 1 };
    cout << sol.amountOfTime(sol.createTree(input, 0), 1) << endl;

    return 0;
}