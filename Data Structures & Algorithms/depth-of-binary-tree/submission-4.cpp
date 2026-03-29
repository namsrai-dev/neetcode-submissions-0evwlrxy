/**
 * Definition for a binary tree node.
 * struct TreeNode {
 * int val;
 * TreeNode *left;
 * TreeNode *right;
 * TreeNode() : val(0), left(nullptr), right(nullptr) {}
 * TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 * TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    int max_depth = 0;

    int maxDepth(TreeNode* root) {
        max_depth = 0; // Reset for each call
        if (root != nullptr) {
            goDepth(1, root);
        }
        return max_depth;
    }

    void goDepth(int n, TreeNode* root) {
        // Update the global maximum depth
        if (n > max_depth) {
            max_depth = n;
        }

        // Recursive calls for children
        if (root->left != nullptr) {
            goDepth(n + 1, root->left);
        }
        if (root->right != nullptr) {
            goDepth(n + 1, root->right);
        }
    }
};