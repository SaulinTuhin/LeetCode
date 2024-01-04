#include <iostream>
#include <cstdlib>

using namespace std;

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution
{
public:
    bool isSameTree(TreeNode *p, TreeNode *q)
    {
        if (!p && !q)
            return true;

        if (p->val == q->val && isSameTree(p->left, q->left) && isSameTree(p->right, q->right))
            return true;

        else
            return false;
    }

    bool isSubtree(TreeNode *root, TreeNode *subRoot)
    {
        if (!root)
            return false;

        if (isSameTree(root, subRoot))
            return true;

        return isSameTree(root->left, subRoot) || isSameTree(root->right, subRoot);
    }
};

TreeNode *newNode(int x)
{
    TreeNode *tmp = (TreeNode *)malloc(sizeof(TreeNode));

    tmp->val = x;

    return tmp;
}

int main()
{
    Solution a;

    TreeNode *root, *subRoot;
    root = newNode(1);
    root->left = newNode(1);

    subRoot = newNode(1);

    cout << a.isSubtree(root, subRoot) << endl;

    return 0;
}